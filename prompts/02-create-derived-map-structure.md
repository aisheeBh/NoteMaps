# 02. Create a new derived map (structure only, no content)

Use this to design a new derived map: its JSON, its branch and its empty folders. It writes no note content. If the new map needs a node the main map lacks, the missing node is added to the main map first, but only where it genuinely belongs there.

```text
Use the NoteMaps repo at C:\abh_pers_od_tfr\NoteMaps\NoteMaps.

Read skills/notemap-content/SKILL.md section 13 (Derived maps) and section 3 (Repository and tools). Then read scripts/derive_gen_ai_and_llms.py and scripts/sync_derived_map.py (read the top of each file; do NOT run scripts with --help, some of them run immediately), and scripts/apply_05_add_math_foundations.py as the pattern for adding nodes to the main map. The existing derived map "Gen AI & LLMs" is the model to follow.

Goal: create a new derived map called "<MAP NAME>" for this learner and purpose: <WHO IT IS FOR, THE STARTING POINT, AND THE END POINT(S) THEY SHOULD REACH>.

Rules:
- Every node in the derived map must be a main-map node: same title text, renumbered for the path (1. / 1.1. / A. / A.1.), with a "source" field on every node giving the main-map title path.
- The order is a strict learning path from absolute novice to expert for the purpose above.
- If the map needs a node that the main map does not have, add it to the MAIN map first (source_json/Professional_Career_Development.json, via a new scripts/apply_NN_*.py file modelled on apply_05), but only where it genuinely belongs and never redundantly or in a way that clogs the main map. Tell me about each such node before adding it.
- Do not write any note content. Folders and empty notes only.
- Ask me questions before you start rather than assume. Give me a short brief of your understanding and the proposed outline (steps, which main-map nodes go in each, and any nodes to be added to main) and wait for my approval before generating anything.

After I approve:
1. If main needs new nodes: write the apply script, run it, run scripts/validate_map.py, then scripts/build_tree_map.py (it only adds folders, never deletes), then scripts/check_alignment.py. Show me the results.
2. Write scripts/derive_<map_slug>.py (modelled on derive_gen_ai_and_llms.py) that generates source_json/<Map_Name>.json.
3. Create the branch derived/<map-slug> and a separate git worktree for it at C:\abh_pers_od_tfr\NoteMaps\NoteMaps-derived-<map-slug>, so the main checkout is never switched.
4. In that worktree run: git merge main, then python scripts/sync_derived_map.py source_json/<Map_Name>.json "derived_maps/<Map Name>", and confirm it prints IDENTICAL TO MAIN MAP.
5. Commit locally. Do not push until I say so.

Report: the number of nodes, the number that already have content, the nodes added to main (if any), and the commands to continue.
```
