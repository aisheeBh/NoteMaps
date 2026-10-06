"""Locate NoteMaps nodes and show everything needed to write their content.

Usage (from the repo root):
    python scripts/find_node.py <query> [<query> ...] [--tree] [--todo]

A query can be:
    root                      the map root
    1.1.1.A.12                a full dotted label (pillar.section.topic.subtopic.leaf)
    1.1.1.A    1.1   3        any shorter full label
    "1.1.1 A.12"              label with a space instead of the dot
    "forgetting curve"        words from a title (case-insensitive; all words must match)
    main_map/.../X.md         a path to a note or node folder

For each matching node it prints: full label, real title (from the JSON, with
? and : restored), kind, note path, whether it is written, its ancestors, its
siblings (for overlap control) and its children (for parent chapters).

    --tree   also print the whole subtree with written/empty status
    --todo   print only the empty notes in the subtree, in reading order
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

SRC = "source_json/Professional_Career_Development.json"
DEST = "main_map"
INVALID = r'<>:"/\\|?*'
KINDS = ["map", "pillar", "section", "topic", "subtopic", "leaf"]


def sanitize(name):
    name = re.sub(f"[{re.escape(INVALID)}]", "-", name)
    return name.rstrip(" .").strip()


def label_of(title):
    m = re.match(r"^([A-Z]+\.\d+\.|[A-Z]+\.|\d+(?:\.\d+)*\.)\s", title)
    return m.group(1).rstrip(".") if m else ""


def build_index():
    data = json.load(open(SRC, encoding="utf-8"))
    nodes = []

    def walk(n, depth, parent, folder):
        fname = sanitize(n["title"])
        path = os.path.join(folder, fname)
        lab = label_of(n["title"])
        if depth == 0:
            full = "root"
        elif depth <= 3:
            full = lab
        elif depth == 4:
            full = f"{parent['full']}.{lab}"
        else:
            full = f"{parent['full'].rsplit('.', 1)[0]}.{lab}"
        node = {
            "title": n["title"], "depth": depth, "kind": KINDS[min(depth, 5)],
            "full": full, "folder": path, "md": os.path.join(path, fname + ".md"),
            "parent": parent, "children": [],
        }
        nodes.append(node)
        for c in n.get("children") or []:
            node["children"].append(walk(c, depth + 1, node, path))
        return node

    for top in data:
        walk(top, 0, None, DEST)
    return nodes


def status(node):
    p = node["md"]
    if not os.path.exists(p):
        return "MISSING ON DISK"
    if os.path.getsize(p) == 0:
        return "empty"
    words = len(re.findall(r"\w+", re.sub(r"```.*?```", "", open(p, encoding="utf-8").read(), flags=re.S)))
    figs = [f for f in os.listdir(node["folder"]) if f.startswith("fig-") and f.endswith(".svg")]
    return f"WRITTEN ({words} words, {len(figs)} SVG figures)"


def match(nodes, q):
    q = q.strip()
    if q.lower() in ("root", "map"):
        return [n for n in nodes if n["depth"] == 0]
    norm = q.replace("\\", "/")
    if norm.endswith(".md") or norm.startswith("main_map"):
        target = os.path.normpath(norm)
        return [n for n in nodes if os.path.normpath(n["md"]) == target or os.path.normpath(n["folder"]) == target]
    lab = re.sub(r"\s+", ".", q).rstrip(".")
    if re.fullmatch(r"\d+(\.\d+)*(\.[A-Z]+(\.\d+)?)?", lab):
        return [n for n in nodes if n["full"] == lab]
    words = [w.lower() for w in re.findall(r"\w+", q)]
    return [n for n in nodes if all(w in n["title"].lower() for w in words)]


def show(n, args):
    print("=" * 78)
    print(f"{n['full']:<14} {n['title']}")
    print(f"kind     : {n['kind']}  (depth {n['depth']})")
    print(f"note     : {n['md']}")
    print(f"status   : {status(n)}")
    own = label_of(n["title"])
    fig_prefix = "fig-" + ("0" if n["depth"] == 0 else own.replace(".", "") if n["depth"] >= 4 else own) + "-"
    print(f"figures  : save as {fig_prefix}<slug>.svg in the node folder")
    chain, p = [], n["parent"]
    while p:
        chain.append(p["title"])
        p = p["parent"]
    if chain:
        print("ancestors:")
        for c in reversed(chain):
            print(f"    {c}")
    if n["parent"]:
        sib = [s for s in n["parent"]["children"] if s is not n]
        print(f"siblings ({len(sib)}) - stay off their core subjects:")
        for s in sib:
            print(f"    {s['title']}")
    if n["children"]:
        print(f"children ({len(n['children'])}) - one or two sentences each at most, never listed:")
        for c in n["children"]:
            print(f"    {c['title']}")
    if args["tree"] or args["todo"]:
        print("subtree:" if args["tree"] else "empty notes in subtree (reading order):")

        def rec(m, ind):
            st = status(m)
            if args["tree"] or st == "empty":
                print(f"    {'  ' * ind}{m['full']:<14} {m['title']}  [{st}]")
            for c in m["children"]:
                rec(c, ind + 1)
        rec(n, 0)


def main():
    argv = sys.argv[1:]
    args = {"tree": "--tree" in argv, "todo": "--todo" in argv}
    queries = [a for a in argv if not a.startswith("--")]
    if not queries:
        print(__doc__)
        sys.exit(2)
    nodes = build_index()
    for q in queries:
        hits = match(nodes, q)
        if not hits:
            print(f"no node matches {q!r}")
            continue
        if len(hits) > 25:
            print(f"{q!r} matches {len(hits)} nodes; showing the first 25 - narrow the query:")
            for h in hits[:25]:
                print(f"    {h['full']:<14} {h['title']}")
            continue
        for h in hits:
            show(h, args)


if __name__ == "__main__":
    main()
