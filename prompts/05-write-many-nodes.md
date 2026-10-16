# 05. Write many notes with parallel agents

Use this for a large batch, such as a whole topic or section. It works one subtopic at a time with a small number of agents, so the laptop stays responsive.

```text
Use the NoteMaps repo at C:\abh_pers_od_tfr\NoteMaps\NoteMaps. Read skills/notemap-content/SKILL.md completely (especially sections 6-12 and 14) and the two reference notes it names.

Write the content for every empty note under: <NODE LABEL, TITLE OR PATH>

How to run it:
- Run python scripts/find_node.py "<node>" --todo to list what is empty. Work one subtopic at a time: its leaves first, then its chapter note.
- Use background agents, ONE agent per subtopic, with AT MOST 3 writing agents at once, so the laptop does not hang. Start the next subtopic only when one finishes.
- Give each agent: the skill file, its exact node labels, the rule that it writes only inside its own node folders, and a list of the sibling subtopics it must stay off. Tell it not to run git commands and not to touch derived_maps/.
- Tell each agent to validate without --render while drafting, preview SVGs in one batch, and run validate_notes.py --render once at the end of its subtopic.
- Each agent must label made-up material "(illustrative)", name study authors only when verified, and report the facts it wrote from memory.
- If an agent stalls, resume it with SendMessage rather than starting a duplicate.
- If the laptop slows down, drop to two agents.

After each subtopic finishes:
- Review the agent's report, then commit that subtopic's folder locally with a clear message (git add only the finished folder).
- Keep a running log of what was written, the facts taken from memory, and any open questions, so I can review them.

Do not push anything until I say so. Never run rm -rf on main_map. When everything is done, give me one summary: notes written, word and figure counts, validation results, the facts to double-check, and any notes under the length target.
```
