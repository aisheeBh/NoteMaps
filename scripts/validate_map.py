"""Validate the source JSON: label scheme, numbering, duplicate titles.
Child counts are NOT checked - a node has as many children as it needs.
"""
import re
import sys
sys.path.insert(0, "scripts")
import _mapkit as mk

LETTERS = mk.LETTERS
errors, warnings = [], []


def check(node, depth, path):
    kids = node.get("children") or []
    titles = [k["title"] for k in kids]

    # duplicate sibling titles (ignoring the label)
    bodies = [mk.body(t).lower() for t in titles]
    for b in set(bodies):
        if bodies.count(b) > 1:
            errors.append(f"DUPLICATE SIBLING {b!r} x{bodies.count(b)} under {path}")

    # label scheme + sequence
    if depth in (0, 1, 2):            # children are numbered N. / N.N. / N.N.N.
        nums = []
        for t in titles:
            m = re.match(r"^(\d+(?:\.\d+)*)\.\s", t)
            if not m:
                errors.append(f"BAD LABEL {t!r} under {path}")
                continue
            nums.append(m.group(1))
        seen = set()
        for n in nums:
            if n in seen:
                errors.append(f"NUMBER COLLISION {n} under {path}")
            seen.add(n)
        last = [int(x) for x in nums[-1].split(".")][-1] if nums else 0
        ints = sorted(int(n.split(".")[-1]) for n in nums)
        if ints and ints != list(range(1, len(ints) + 1)):
            missing = set(range(1, max(ints) + 1)) - set(ints)
            if missing:
                warnings.append(f"NON-CONTIGUOUS under {path}: missing {sorted(missing)}")
    elif depth == 3:                  # children are lettered A. B. C.
        for i, t in enumerate(titles):
            want = LETTERS[i] + "."
            if not t.startswith(want + " "):
                errors.append(f"BAD LETTER {t!r} (expected {want}) under {path}")
    elif depth == 4:                  # children are X.1 X.2 ...
        letter = mk.label(node["title"]).rstrip(".")
        for i, t in enumerate(titles, 1):
            want = f"{letter}.{i}."
            if not t.startswith(want + " "):
                errors.append(f"BAD NOTE LABEL {t!r} (expected {want}) under {path}")
    elif depth == 5 and kids:
        errors.append(f"UNEXPECTED CHILDREN at depth 5: {path}")

    for k in kids:
        check(k, depth + 1, path + " > " + k["title"])


data = mk.load()
r = mk.root(data)
check(r, 0, r["title"])

# global: topic titles duplicated anywhere
from collections import Counter
topics = [n["title"] for n, d, _ in mk.walk(r) if d == 3]
dupes = {mk.body(t).lower() for t in topics
         if [mk.body(x).lower() for x in topics].count(mk.body(t).lower()) > 1}
for d in sorted(dupes):
    where = [t for t in topics if mk.body(t).lower() == d]
    warnings.append(f"TOPIC TITLE REUSED: {d!r} -> {where}")

print(f"counts by depth: {mk.counts(data)}")
print(f"\n{len(errors)} errors, {len(warnings)} warnings")
for e in errors[:40]:
    print("  ERROR  ", e)
for w in warnings[:40]:
    print("  WARN   ", w)
sys.exit(1 if errors else 0)
