# 07. Label made-up material as illustrative

Use this on notes written before the labelling rule, or on any note where invented cases, people, organisations or numbers are not marked. It changes labels only, never wording or structure.

```text
Use the NoteMaps repo at C:\abh_pers_od_tfr\NoteMaps\NoteMaps. Read skills/notemap-content/SKILL.md section 1 rule 5 (illustrative material).

Rule: anything made up must be marked "illustrative". Go through every written note under: <NODE LABEL, TITLE OR PATH>

For each note:
1. Find every case study, scenario, worked example, example organisation or person, table, and figure caption that describes an invented organisation, person, event or data.
2. Label them:
   - Headings: "### Case study: X" becomes "### Case study (illustrative): X"; the same for Worked example, Scenario, and bold pseudo-headings.
   - Boxes and bullets about an invented incident: "> **Example (illustrative):** ..."
   - Tables of invented numbers: add a blank line and then "*Illustrative figures.*" directly under the table (unless the text right after already says so).
   - Figure captions for SVGs that show invented data: append " (illustrative)" after the final full stop of the "**Figure N.**" caption.
3. Do NOT label real, documented events, real studies, or real named organisations' documented actions. When unsure whether something is real, check the surrounding text; if it is presented as a composite or has no verifiable source, label it.
4. Leave generic hypothetical opening hooks and Self-Check questions unlabelled. Leave plan or schedule tables with no invented data unlabelled. Leave computed model curves unlabelled when their small print says so.
5. Change nothing else: no rewording, no restructuring, no new content. Preserve each file's line endings.
6. After each folder, run python scripts/validate_notes.py "<folder>" (no --render) and make sure there are 0 errors.

For several folders, use at most 2 agents at a time. Do not run git commands and do not touch derived_maps/. Report, per folder, the number of labels added and anything you were unsure about.
```
