# 11. Commit and push

Use this only when you want work sent to GitHub. Nothing in the other prompts pushes. Pasting this prompt is your approval to push exactly what it says.

```text
Use the NoteMaps repo at C:\abh_pers_od_tfr\NoteMaps\NoteMaps. I approve pushing the following and nothing else: <main | the derived branch derived/<map-slug> | both>.

Steps:
1. Show me git status -sb for main and for the derived worktree (C:\abh_pers_od_tfr\NoteMaps\NoteMaps-derived for "Gen AI & LLMs"), and any uncommitted changes. If there are uncommitted note changes, list them and commit them first, staging only finished folders, with clear messages.
2. If the derived map must be updated first, do that with the sync procedure in skills/notemap-content/SKILL.md section 13 (git merge main, run the sync script, confirm IDENTICAL TO MAIN MAP, commit derived_maps).
3. Push with a normal git push origin <branch>. Never force-push. If the push fails with an HTTP 408 or a disconnect because the upload is large, retry once; if it still fails, push the derived branch first (it contains main's commits) and then push main, and tell me what happened.
4. Confirm that git status -sb shows each branch level with origin.

Report what was pushed and the final commit on each branch.
```
