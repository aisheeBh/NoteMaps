# 04. Add new nodes to the main map (no content)

Use this to add a new topic, subtopic or leaf to the main map. It changes structure only. Note content is written afterwards with prompt 01.

```text
Use the NoteMaps repo at C:\abh_pers_od_tfr\NoteMaps\NoteMaps.

Read skills/notemap-content/SKILL.md section 3 (labels and layout). Read the top of scripts/_mapkit.py, scripts/apply_05_add_math_foundations.py (the pattern to follow), scripts/validate_map.py, scripts/build_tree_map.py and scripts/check_alignment.py. Do NOT run scripts with --help; some of them run immediately.

Add these nodes to the main map: <WHAT TO ADD AND WHERE, e.g. "a new topic 3.2.22 'X' under section 3.2 with these subtopics ...">

Rules:
- Before changing anything, check the main map for an existing node that already covers this, and tell me what you found. Do not create a redundant or overlapping node. If something similar exists, ask me.
- Ask me questions rather than assume. Show me the exact nodes you plan to add (labels, titles, parent) and wait for approval.
- Follow the label scheme: Section N.N., Topic N.N.N., Subtopic A., Leaf A.1., and keep numbering sequential with the siblings.
- Write a new scripts/apply_NN_<short_name>.py that makes the change through scripts/_mapkit.py, so the change is repeatable and reviewable. Keep a backup copy of the JSON before running it.
- After running it, run scripts/validate_map.py, then scripts/build_tree_map.py (it only adds folders, it never deletes), then scripts/check_alignment.py. All three must be clean.
- Never run rm -rf on main_map. If a rename leaves a stale folder, tell me and ask before removing anything.
- Commit locally with a clear message. Do not push until I say so.

Report: the nodes added, the check results, and which derived maps (if any) now need the new nodes.
```
