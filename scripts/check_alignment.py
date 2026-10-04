"""Verify main_map/ is an exact mirror of the source JSON.

Reports anything present in one and not the other. Because the generator is
additive-only, a stale folder left over from a rename shows up here as
EXTRA-ON-DISK.
"""
import os
import re
import sys
sys.path.insert(0, "scripts")
import _mapkit as mk

DEST = "main_map"
INVALID = r'<>:"/\\|?*'


def sanitize(name):
    name = re.sub(f"[{re.escape(INVALID)}]", "-", name)
    return name.rstrip(" .").strip()


expected_dirs, expected_files = set(), set()


def expect(node, parent):
    title = sanitize(node["title"])
    kids = node.get("children") or []
    if kids:
        folder = os.path.join(parent, title)
        expected_dirs.add(folder)
        expected_files.add(os.path.join(folder, title + ".md"))
        for k in kids:
            expect(k, folder)
    else:
        expected_files.add(os.path.join(parent, title + ".md"))


data = mk.load()
for n in data:
    expect(n, DEST)

actual_dirs, actual_files = set(), set()
for root, dirs, files in os.walk(DEST):
    for d in dirs:
        actual_dirs.add(os.path.join(root, d))
    for f in files:
        actual_files.add(os.path.join(root, f))

md = {f for f in actual_files if f.endswith(".md")}
non_md = actual_files - md

missing_d = expected_dirs - actual_dirs
extra_d = actual_dirs - expected_dirs
missing_f = expected_files - md
extra_f = md - expected_files

print(f"JSON  : {len(expected_dirs):>6} folders  {len(expected_files):>7} md files")
print(f"DISK  : {len(actual_dirs):>6} folders  {len(md):>7} md files")
print()
print(f"missing folders (in JSON, not on disk) : {len(missing_d)}")
print(f"EXTRA folders   (on disk, not in JSON) : {len(extra_d)}")
print(f"missing files   (in JSON, not on disk) : {len(missing_f)}")
print(f"EXTRA files     (on disk, not in JSON) : {len(extra_f)}")
if non_md:
    print(f"non-markdown files on disk             : {len(non_md)}")

for label, s in (("MISSING DIR", missing_d), ("EXTRA DIR", extra_d),
                 ("MISSING FILE", missing_f), ("EXTRA FILE", extra_f)):
    for p in sorted(s)[:10]:
        print(f"  {label}: {p}")

ok = not (missing_d or extra_d or missing_f or extra_f)
print("\nALIGNED" if ok else "\nNOT ALIGNED")
sys.exit(0 if ok else 1)
