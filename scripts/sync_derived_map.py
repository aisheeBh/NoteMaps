"""Generate a derived map's folders and copy its content exactly from main_map.

A derived map is defined by a JSON file whose nodes look like
    {"title": "<renumbered title>", "source": [<main-map titles, root..node>],
     "children": [...]}
Every node is an existing main-map node. This script:
  1. creates one folder per derived node, holding <title>.md (same layout as
     main_map);
  2. copies each source note's content byte-for-byte, plus every fig-*.svg in
     the source node's folder;
  3. removes files and folders that no longer belong to the derived map
     (derived maps hold no hand-written content, so this is always safe);
  4. verifies that every derived note and figure is identical to its source.

Run it again whenever main-map content changes.

Usage:
    python scripts/sync_derived_map.py source_json/Gen_AI_and_LLMs.json "derived_maps/Gen AI & LLMs"
    python scripts/sync_derived_map.py <json> <dest> --check     # verify only
    python scripts/sync_derived_map.py <json> <dest> --todo      # empty notes, in path order,
                                                                 # with the main-map node to write
"""
import filecmp
import json
import os
import re
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")

MAIN_JSON = "source_json/Professional_Career_Development.json"
MAIN_DIR = "main_map"
INVALID = r'<>:"/\\|?*'


def sanitize(name):
    name = re.sub(f"[{re.escape(INVALID)}]", "-", name)
    return name.rstrip(" .").strip()


def body(title):
    m = re.match(r"^([A-Z]+\.\d+\.|[A-Z]+\.|\d+(?:\.\d+)*\.)\s", title)
    return title[m.end():].strip() if m else title.strip()


def main_titles():
    """Set of title-paths that exist in the main JSON."""
    data = json.load(open(MAIN_JSON, encoding="utf-8"))
    paths = set()

    def walk(n, p):
        q = p + (n["title"],)
        paths.add(q)
        for c in n.get("children") or []:
            walk(c, q)
    for r in data:
        walk(r, ())
    return paths


def source_dir(src):
    return os.path.join(MAIN_DIR, *[sanitize(t) for t in src])


def plan(node, parent_dir, out, errors, known):
    name = sanitize(node["title"])
    folder = os.path.join(parent_dir, name)
    src = tuple(node["source"])
    if src not in known:
        errors.append(f"source not in main map: {' > '.join(src)}")
    elif body(node["title"]) != body(src[-1]):
        errors.append(f"title text differs from source: {node['title']!r} vs {src[-1]!r}")
    sdir = source_dir(src)
    out.append((folder, os.path.join(folder, name + ".md"),
                sdir, os.path.join(sdir, sanitize(src[-1]) + ".md")))
    for c in node.get("children") or []:
        plan(c, folder, out, errors, known)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check_only = "--check" in sys.argv or "--todo" in sys.argv
    if len(args) != 2:
        print(__doc__)
        sys.exit(2)
    spec, dest = args
    data = json.load(open(spec, encoding="utf-8"))
    known = main_titles()
    items, errors = [], []
    for r in data:
        plan(r, dest, items, errors, known)
    if errors:
        for e in errors[:20]:
            print("ERROR", e)
        sys.exit(f"{len(errors)} structural errors - fix the derived JSON first")

    if "--todo" in sys.argv:
        todo = [(md, smd) for _, md, _, smd in items
                if not os.path.exists(smd) or os.path.getsize(smd) == 0]
        for md, smd in todo:
            print(f"{os.path.relpath(md, dest)}\n    write in main map: {smd}")
        print(f"\n{len(todo)} of {len(items)} derived notes still need main-map content")
        return

    want_files, want_dirs = set(), set()
    copied = figs = 0
    for folder, md, sdir, smd in items:
        want_dirs.add(os.path.normpath(folder))
        want_files.add(os.path.normpath(md))
        src_figs = sorted(f for f in os.listdir(sdir)
                          if f.startswith("fig-") and f.endswith(".svg")) if os.path.isdir(sdir) else []
        for f in src_figs:
            want_files.add(os.path.normpath(os.path.join(folder, f)))
        if check_only:
            continue
        os.makedirs(folder, exist_ok=True)
        if not os.path.exists(md) or not filecmp.cmp(smd, md, shallow=False):
            shutil.copyfile(smd, md)
            copied += 1
        for f in src_figs:
            s, d = os.path.join(sdir, f), os.path.join(folder, f)
            if not os.path.exists(d) or not filecmp.cmp(s, d, shallow=False):
                shutil.copyfile(s, d)
                figs += 1

    # remove anything that no longer belongs to the derived map
    removed = 0
    if not check_only and os.path.isdir(dest):
        for root, dirs, files in os.walk(dest, topdown=False):
            for f in files:
                p = os.path.normpath(os.path.join(root, f))
                if p not in want_files:
                    os.remove(p)
                    removed += 1
            if os.path.normpath(root) not in want_dirs and os.path.normpath(root) != os.path.normpath(dest):
                if not os.listdir(root):
                    os.rmdir(root)

    # verify
    bad = []
    for folder, md, sdir, smd in items:
        if not os.path.exists(md) or not filecmp.cmp(smd, md, shallow=False):
            bad.append(md)
        if os.path.isdir(sdir):
            for f in os.listdir(sdir):
                if f.startswith("fig-") and f.endswith(".svg"):
                    d = os.path.join(folder, f)
                    if not os.path.exists(d) or not filecmp.cmp(os.path.join(sdir, f), d, shallow=False):
                        bad.append(d)
    written = sum(1 for _, md, _, _ in items if os.path.exists(md) and os.path.getsize(md) > 0)
    print(f"{len(items)} nodes | {written} with content | "
          f"{copied} notes and {figs} figures copied | {removed} stale files removed")
    if bad:
        for b in bad[:20]:
            print("NOT IDENTICAL", b)
        sys.exit(f"{len(bad)} files differ from their main-map source")
    print("IDENTICAL TO MAIN MAP")


if __name__ == "__main__":
    main()
