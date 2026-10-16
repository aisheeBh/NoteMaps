# 08. Verify facts that were written from memory

Use this to check the specific facts a writer flagged as "from memory", or to spot-check a note you are about to rely on. It corrects or rewords what it cannot confirm.

```text
Use the NoteMaps repo at C:\abh_pers_od_tfr\NoteMaps\NoteMaps. Read skills/notemap-content/SKILL.md section 9 (research and truthfulness).

Verify the facts in: <NOTE PATHS OR NODE LABELS, AND OPTIONALLY THE SPECIFIC CLAIMS TO CHECK>

For each study, statistic, date, law, court case, quotation and named person in the notes:
1. Web-search it. Confirm the claim, the figure, the year and the people or institution involved.
2. If it is confirmed, leave it.
3. If it is wrong, correct it in the note.
4. If it cannot be confirmed, do not leave it as fact. Reword it so it is true and general (describe a study by institution, venue or year instead of by invented author names; give a range or "roughly" instead of a precise figure you cannot support), or remove it. Never invent a source.
5. Keep the rest of the note unchanged, including its figures and numbering. Where a correction changes a diagram or an SVG, fix that too.
6. Do not add links or references that send the reader elsewhere. Names, dates and figures explained in the text are fine.

After editing, run python scripts/validate_notes.py "<note or folder>" --render and fix any errors.

Report as a table: claim, where it appears, what you found, and what you changed. Do not run git commands and do not touch derived_maps/.
```
