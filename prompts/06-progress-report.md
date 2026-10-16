# 06. Progress report

Use this at the start of a session, or whenever you want to know where things stand. It only reads; it changes nothing.

```text
Use the NoteMaps repo at C:\abh_pers_od_tfr\NoteMaps\NoteMaps. Read skills/notemap-content/SKILL.md sections 3 and 13. Do not change any file, run git commit or push, or start any agent. This is a read-only report.

Tell me:
1. For the main map: how many notes have content and how many are empty, by section (use python scripts/find_node.py "<section label>" --tree, or --todo, section by section such as 1.1, 1.2, 1.6).
2. For the derived map "<MAP NAME>" (or every derived map under derived_maps/ on its branch): how many of its nodes have content and how many are empty. Use python scripts/sync_derived_map.py source_json/<Map_Name>.json "derived_maps/<Map Name>" --todo from its worktree, and list the first 20 empty notes in learning order with the main-map file to write for each. Do not run the sync script without --todo or --check.
3. Whether main and the derived map are identical (python scripts/sync_derived_map.py <json> <dest> --check).
4. Git state: how many commits main and each derived branch are ahead of origin (git status -sb), and whether anything is uncommitted.
5. Any notes under the length target (about 4,000 words for a leaf, 4,500 for a chapter) that would be good top-ups.
6. A recommended next step, in one or two sentences.

Keep the report short and use a table where it helps.
```
