# 03. Copy finished main-map content into a derived map

Use this after notes have been written on `main`. It copies every available main-map note and figure into the derived map, byte for byte, and verifies the copies. It never writes new content.

```text
Use the NoteMaps repo at C:\abh_pers_od_tfr\NoteMaps\NoteMaps. Read skills/notemap-content/SKILL.md section 13 (Derived maps).

Update the derived map "<MAP NAME>" so that every note it has in common with the main map is an exact copy of the main-map note, along with its fig-*.svg files.

Steps:
1. Check that main has no uncommitted note changes (git status). If it has, stop and tell me.
2. Use the derived map's worktree (C:\abh_pers_od_tfr\NoteMaps\NoteMaps-derived for "Gen AI & LLMs", otherwise the worktree for branch derived/<map-slug>; create one with git worktree add if none exists). Do not switch branches in the main checkout.
3. In that worktree: git merge main.
4. Run: python scripts/sync_derived_map.py source_json/<Map_Name>.json "derived_maps/<Map Name>"
   Confirm it prints IDENTICAL TO MAIN MAP. If it does not, stop and tell me which notes differ.
5. Commit only derived_maps in that worktree with a message such as "Sync derived map <Map Name> with main". Do not push until I say so.

Rules:
- Never edit anything inside derived_maps/ by hand. The sync script is the only thing that writes there.
- Never copy a note that is empty on main; the script leaves those empty on purpose.

Report: how many nodes have content now, how many notes and figures were copied, and the result of the identical check.
```

To see which notes in the derived map are still empty, and which main-map file to write for each, run `python scripts/sync_derived_map.py source_json/<Map_Name>.json "derived_maps/<Map Name>" --todo`. Prompt 06 does this for you.
