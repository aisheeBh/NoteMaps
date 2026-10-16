# 10. Validate notes and repair what fails

Use this when you want every written note checked against the format rules and fixed. It repairs problems; it does not rewrite content.

```text
Use the NoteMaps repo at C:\abh_pers_od_tfr\NoteMaps\NoteMaps. Read skills/notemap-content/SKILL.md section 10 (validation) and section 11 (definition of done).

Check and repair the notes under: <NODE LABEL, TITLE OR PATH, OR "the whole main map">

Steps:
1. Run python scripts/validate_notes.py "<folder>" without --render first, one subtopic at a time. Collect the errors and warnings.
2. Fix every error. Fix every warning unless it is a proper noun the checker misreads (for example "Organization" in a real organisation's name, or an author's surname); leave those and list them for me.
3. Run python scripts/validate_notes.py "<folder>" --render once per subtopic to confirm every Mermaid diagram draws. If a diagram fails, repair its syntax (for example thick-arrow label syntax or semicolons inside sequence-diagram messages) and re-run.
4. Check that each note has at least 5 numbered figures, at least one case study and one worked example, and that figure numbering is sequential. Report notes that fall short; do not invent new sections without asking.
5. Run python scripts/check_alignment.py to confirm the folders still mirror the JSON.

Do not change the meaning of any sentence. Do not run git commands and do not touch derived_maps/. For many folders use at most 2 agents at a time.

Report: notes checked, errors and warnings found and fixed, anything left and why.
```
