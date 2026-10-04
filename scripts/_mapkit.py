"""Shared helpers for editing the NoteMaps source JSON.

The JSON is the source of truth: [{"title": str, "children": [...]}].
Every operation here works on that tree and preserves the labelling scheme
(N.N.N. at depth 3, letters at depth 4, letter.N at depth 5).
Child counts are deliberately NOT normalised - a node has as many children
as its subject needs.
"""
import json
import re

SRC = "source_json/Professional_Career_Development.json"
LETTERS = [chr(c) for c in range(ord("A"), ord("Z") + 1)]


def load():
    with open(SRC, encoding="utf-8") as f:
        return json.load(f)


def save(data):
    with open(SRC, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)


def root(data):
    return data[0]


def walk(node, depth=0, parent=None):
    yield node, depth, parent
    for c in node.get("children") or []:
        yield from walk(c, depth + 1, node)


def find(node, prefix):
    """Find the single node whose title starts with `prefix`."""
    hits = [n for n, _, _ in walk(node) if n["title"].startswith(prefix)]
    if len(hits) != 1:
        raise LookupError(f"{prefix!r} matched {len(hits)} nodes: "
                          f"{[h['title'] for h in hits][:5]}")
    return hits[0]


def find_parent(node, prefix):
    for n, _, p in walk(node):
        if n["title"].startswith(prefix) and p is not None:
            return p
    raise LookupError(f"no parent for {prefix!r}")


def label(title):
    """'3.2.14. Prompt Engineering' -> '3.2.14.'  /  'C. RAG' -> 'C.'"""
    m = re.match(r"^([A-Z]+\.|[\d.]+\.)\s", title)
    return m.group(1) if m else ""


def body(title):
    return title[len(label(title)):].strip()


def rename(node, prefix, new_title):
    n = find(node, prefix)
    old = n["title"]
    n["title"] = new_title
    return old, new_title


def retitle_body(node, prefix, new_body):
    """Keep the existing number/letter, replace only the text after it."""
    n = find(node, prefix)
    old = n["title"]
    n["title"] = f"{label(old)} {new_body}"
    return old, n["title"]


def notes(letter, items):
    return [{"title": f"{letter}.{i}. {t}", "children": []}
            for i, t in enumerate(items, 1)]


def subtopic(letter, title, items):
    return {"title": f"{letter}. {title}", "children": notes(letter, items)}


def make_topic(number, title, subs):
    """subs: list of (subtopic_title, [12 note titles])"""
    return {
        "title": f"{number}. {title}",
        "children": [subtopic(LETTERS[i], st, items)
                     for i, (st, items) in enumerate(subs)],
    }


def reletter(node):
    """Re-letter a topic's subtopics A,B,C... and their notes, after a removal."""
    for i, sub in enumerate(node.get("children") or []):
        new = LETTERS[i]
        sub["title"] = f"{new}. {body(sub['title'])}"
        for j, leaf in enumerate(sub.get("children") or [], 1):
            leaf["title"] = f"{new}.{j}. {body(leaf['title'])}"


def drop_subtopic(node, topic_prefix, sub_body):
    """Remove a subtopic by its text, then re-letter siblings."""
    topic = find(node, topic_prefix)
    before = len(topic["children"])
    topic["children"] = [c for c in topic["children"]
                         if body(c["title"]).lower() != sub_body.lower()]
    if len(topic["children"]) == before:
        raise LookupError(f"{sub_body!r} not found under {topic_prefix}")
    reletter(topic)
    return topic["title"]


def add_subtopic(node, topic_prefix, title, items):
    topic = find(node, topic_prefix)
    nxt = LETTERS[len(topic["children"])]
    topic["children"].append(subtopic(nxt, title, items))
    return f"{topic['title']} > {nxt}. {title}"


def add_topic(node, section_prefix, number, title, subs):
    section = find(node, section_prefix)
    section["children"].append(make_topic(number, title, subs))
    section["children"].sort(key=lambda c: _numkey(c["title"]))
    return f"{section['title']} > {number}. {title}"


def _numkey(title):
    m = re.match(r"^([\d.]+)\.", title)
    return [int(p) for p in m.group(1).split(".")] if m else [999]


def stub(node, prefix, new_body, canonical_prefix, canonical_label=None):
    """Collapse a redundant topic into a pointer stub, mirroring the map's
    own '- Overview' idiom: one 'A. Overview' subtopic whose notes summarise
    the canonical topic, ending in a pointer to it."""
    target = find(node, prefix)
    canon = find(node, canonical_prefix)
    canon_subs = [body(c["title"]) for c in (canon.get("children") or [])]

    if canon_subs:                      # canonical is a topic -> list its subtopics
        items = canon_subs[:11]
    else:
        items = []
    ref = canonical_label or canonical_prefix.rstrip(".")
    items = items + [f"Full depth covered in Section {ref}"]

    target["title"] = f"{label(target['title'])} {new_body} — Overview"
    target["children"] = [subtopic("A", "Overview", items)]
    return target["title"]


def counts(data):
    from collections import Counter
    c = Counter()
    for n, d, _ in walk(root(data)):
        c[d] += 1
    return dict(sorted(c.items()))
