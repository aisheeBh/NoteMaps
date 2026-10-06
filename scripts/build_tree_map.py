import json
import os
import re
import sys

SRC = r"C:\abh_pers_od_tfr\NoteMaps\NoteMaps\source_json\Professional_Career_Development.json"
DEST_ROOT = r"C:\abh_pers_od_tfr\NoteMaps\NoteMaps\main_map"

INVALID_CHARS = r'<>:"/\\|?*'


def sanitize(name: str) -> str:
    name = re.sub(f"[{re.escape(INVALID_CHARS)}]", "-", name)
    name = name.rstrip(" .")
    return name.strip()


def build(node, parent_dir):
    # Every node - parent or leaf - gets its own folder holding its note
    # (<title>/<title>.md) and any artefacts such as fig-*.svg figures.
    title = sanitize(node["title"])
    children = node.get("children") or []

    folder_path = os.path.join(parent_dir, title)
    os.makedirs(folder_path, exist_ok=True)

    md_path = os.path.join(folder_path, title + ".md")
    if not os.path.exists(md_path):
        open(md_path, "w", encoding="utf-8").close()

    for child in children:
        build(child, folder_path)


def main():
    with open(SRC, "r", encoding="utf-8") as f:
        data = json.load(f)

    os.makedirs(DEST_ROOT, exist_ok=True)

    nodes = data if isinstance(data, list) else [data]
    for node in nodes:
        build(node, DEST_ROOT)

    total_files = 0
    total_dirs = 0
    for _, dirs, files in os.walk(DEST_ROOT):
        total_dirs += len(dirs)
        total_files += len(files)

    print(f"Done. Created {total_dirs} folders and {total_files} md files under {DEST_ROOT}")


if __name__ == "__main__":
    main()
