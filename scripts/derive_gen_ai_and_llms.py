"""Build source_json/Gen_AI_and_LLMs.json - the "Gen AI & LLMs" derived map.

Every node is an existing main-map node, arranged as a learning path from
absolute novice to expert (builder, researcher, product leader, power user).
Titles keep the main-map text but are renumbered for the path:

    root      plain title            (main 1.6.4 Generative AI in Daily Life)
    depth 1   N.     a main section  (a step of the path)
    depth 2   N.N.   a main topic, or a main subtopic placed directly in the step
    depth 3   A.     a main subtopic (re-lettered) - or a note of a placed subtopic
    depth 4   A.1.   a main note

Each node carries "source": the list of real main-map titles from the main
root down to the node it copies. scripts/sync_derived_map.py uses it to copy
note content and figures exactly. Outline approved by the repo owner on
2026-10-07.

Usage: python scripts/derive_gen_ai_and_llms.py
"""
import json
import sys

sys.path.insert(0, "scripts")
import _mapkit as mk

OUT = "source_json/Gen_AI_and_LLMs.json"
LETTERS = mk.LETTERS
ALL = None                 # include every subtopic of a topic
SUBTOPICS = "subtopics"    # place a topic's subtopics directly in the step

ROOT = "1.6.4."            # Generative AI in Daily Life - the novice front door

# (section, [(topic, selection), ...]) in learning order.
STEPS = [
    ("1.1.", [("1.1.1.", ["A", "K"]),
              ("1.1.2.", ["A", "B", "C", "D", "E", "F", "G", "L"]),
              ("1.1.4.", ["C", "G", "H"])]),
    ("1.2.", [("1.2.1.", ["B", "E", "F"]),
              ("1.2.6.", ALL)]),
    ("1.6.", [("1.6.1.", ALL),
              ("1.6.2.", ["A", "B", "C", "D", "G", "H"]),
              ("1.6.3.", ALL),
              ("1.6.4.", SUBTOPICS),        # its chapter is the root note
              ("1.6.9.", ALL),
              ("1.6.13.", ALL),
              ("1.6.11.", ALL),
              ("1.6.6.", ALL),
              ("1.6.7.", ALL),
              ("1.6.8.", ALL)]),
    ("4.10.", [("4.10.4.", ALL), ("4.10.10.", ALL),
               ("4.10.12.", ALL), ("4.10.13.", ALL)]),
    ("1.4.", [("1.4.1.", ["A", "B", "G"]),
              ("1.4.2.", ["B", "C", "F"]),
              ("1.4.9.", ALL)]),
    ("2.1.", [("2.1.1.", ALL),
              ("2.1.3.", ["A", "B", "C", "D", "E", "F"]),
              ("2.1.4.", ALL)]),
    ("2.2.", [("2.2.1.", ALL), ("2.2.2.", ALL), ("2.2.3.", ALL), ("2.2.4.", ALL),
              ("2.2.7.", ["A", "B", "C", "D", "E", "F", "G"]),
              ("2.2.8.", ["A", "B", "C", "D", "I", "L"])]),
    ("2.5.", [("2.5.3.", ["A", "B", "C", "D", "E", "F", "H", "I"])]),
    ("2.11.", [("2.11.13.", ALL),
               ("2.11.6.", ["A", "B", "C", "E", "F", "G", "I", "J"]),
               ("2.11.7.", ["A", "B", "C", "D", "E", "G", "I"]),
               ("2.11.8.", ["A", "B", "C", "D", "E", "F", "H", "L"]),
               ("2.11.9.", ["A", "D", "F"])]),
    ("2.4.", [("2.4.1.", ALL),
              ("2.4.2.", ["A", "B", "E", "G"]),
              ("2.4.7.", ["A", "B", "C", "D"])]),
    ("3.2.", [("3.2.4.", ALL), ("3.2.6.", ALL), ("3.2.7.", ALL),
              ("3.2.9.", ALL), ("3.2.13.", ALL), ("3.2.14.", ALL),
              ("3.2.10.", ALL), ("3.2.20.", ALL), ("3.2.15.", ALL),
              ("3.2.11.", ALL), ("3.2.21.", ALL), ("3.2.19.", ALL),
              ("3.2.16.", ALL), ("3.2.12.", ALL)]),
    ("2.12.", [("2.12.13.", ALL)]),
    ("3.13.", [("3.13.11.", ALL)]),
    ("1.8.", [("1.8.9.", ALL)]),
    ("3.14.", [("3.14.9.", ALL), ("3.14.6.", ALL), ("3.14.7.", ALL)]),
    ("3.4.", [("3.4.13.", ALL)]),
    ("3.5.", [("3.5.14.", ALL)]),
    ("3.8.", [("3.8.15.", ALL), ("3.8.14.", ALL)]),
    ("3.11.", [("3.11.13.", ALL)]),
    ("5.9.", [("5.9.1.", ALL), ("5.9.5.", ALL)]),
    ("5.12.", [("5.12.10.", ALL)]),
]


def index(root):
    """title -> (node, path of titles from the main root)."""
    paths = {}

    def walk(n, path):
        p = path + [n["title"]]
        paths[id(n)] = p
        for c in n.get("children") or []:
            walk(c, p)
    walk(root, [])
    return paths


def node(title, src, paths, children=None):
    return {"title": title, "source": paths[id(src)], "children": children or []}


def leaves(sub, letter, paths):
    return [node(f"{letter}.{j}. {mk.body(n['title'])}", n, paths)
            for j, n in enumerate(sub.get("children") or [], 1)]


def build():
    data = mk.load()
    main_root = mk.root(data)
    paths = index(main_root)
    root_src = mk.find(main_root, ROOT)
    root = node(mk.body(root_src["title"]), root_src, paths)

    seen = set()
    for si, (sec_label, topics) in enumerate(STEPS, 1):
        sec = mk.find(main_root, sec_label + " ")
        step = node(f"{si}. {mk.body(sec['title'])}", sec, paths)
        ti = 0
        for top_label, sel in topics:
            top = mk.find(main_root, top_label + " ")
            subs = top.get("children") or []
            if sel == SUBTOPICS:
                for sub in subs:            # each subtopic becomes its own N.N. entry
                    ti += 1
                    entry = node(f"{si}.{ti}. {mk.body(sub['title'])}", sub, paths)
                    entry["children"] = [
                        node(f"{LETTERS[k]}. {mk.body(n['title'])}", n, paths)
                        for k, n in enumerate(sub.get("children") or [])]
                    step["children"].append(entry)
                continue
            ti += 1
            entry = node(f"{si}.{ti}. {mk.body(top['title'])}", top, paths)
            chosen = subs if sel is ALL else [
                s for s in subs if mk.label(s["title"]).rstrip(".") in sel]
            if sel is not ALL:
                missing = set(sel) - {mk.label(s["title"]).rstrip(".") for s in chosen}
                if missing:
                    raise SystemExit(f"{top['title']}: no subtopics {sorted(missing)}")
            for k, sub in enumerate(chosen):
                letter = LETTERS[k]
                entry["children"].append(node(
                    f"{letter}. {mk.body(sub['title'])}", sub, paths,
                    leaves(sub, letter, paths)))
            step["children"].append(entry)
        root["children"].append(step)

    # every source must be unique, so no main-map node appears twice
    def walk(n):
        key = tuple(n["source"])
        if key in seen:
            raise SystemExit(f"duplicate source: {' > '.join(key)}")
        seen.add(key)
        for c in n["children"]:
            walk(c)
    walk(root)

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump([root], f, ensure_ascii=False, indent=1)

    counts = {}

    def count(n, d):
        counts[d] = counts.get(d, 0) + 1
        for c in n["children"]:
            count(c, d + 1)
    count(root, 0)
    print(f"wrote {OUT}: {sum(counts.values())} nodes, by depth {counts}")


if __name__ == "__main__":
    build()
