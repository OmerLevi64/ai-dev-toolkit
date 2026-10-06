# Dynamic Workflows — Starter Guide

[GitHub dynamic workflows](https://github.blog/changelog/2026-10-01-dynamic-workflows-in-copilot-cli-and-the-copilot-app/) (public preview, Oct 2026 — subject to change) pin a multi-agent process down in code, so Copilot runs the same steps every time instead of improvising a fresh plan from each prompt.

This repo's prompt templates (`prompts/`) drive an agent with words. Dynamic workflows are the next layer: the *process itself* becomes a program.

## When to use a workflow vs. a prompt

| | Prompt template | Dynamic workflow |
|---|---|---|
| Best for | One-shot tasks, quick answers | Repeatable, multi-stage processes |
| Structure | Free-form text | Steps in code: sequential, parallel, or both |
| Judgment | All in the model's head | Agents analyze; code orchestrates |
| Human control | You steer every turn | Checkpoints pause for review; resume when ready |

GitHub's rule of thumb: for a quick answer or a simple change, a normal prompt is sufficient. Reach for a workflow when the process is reusable, or when a task needs clear stages, checks, or limits.

## What workflows can do

- Run commands, use tools, or call other services
- Split a goal into parallel tasks and run them concurrently
- Pass structured results from one stage to the next
- Have subagents verify each other's findings
- Ask you for input (if your client supports it)
- Pause at a checkpoint so you can review results, then resume

## Creating a workflow

You describe the process; Copilot authors the program (or follow its built-in authoring guidance to write it yourself — ask Copilot: *"Show me the guidance for writing dynamic workflows"*).

1. In a Copilot session, describe what the workflow should accomplish, the order of steps, which parts need an agent, and any limits:

   ```text
   Create a dynamic workflow named release-check that gathers the changes
   since the last tag, runs the release checks, asks one agent to assess
   any failures, and pauses for me to review the findings before resuming.
   ```

2. Approve the authoring when prompted (and any follow-up approvals).
3. Verify it registered: ask *"What dynamic workflows are available?"*

By default the workflow lives in an extension for the current session only. To keep it, copy its extension directory to `~/.copilot/extensions/` (personal, all your sessions) or your repo's `.github/extensions/` (project, shared with the team) — ask Copilot for the path first, e.g. *"Tell me the path to the release-check dynamic workflow."*

## Running a workflow

In chat:

```text
Run the release-check dynamic workflow for version 0.3.0, with an AI credit limit of 300.
```

In the CLI (requires experimental features — run with `--experimental` or `/experimental on`):

```bash
copilot workflow run release-check \
  --args '{"version":"0.3.0"}' \
  --allow-tool=read
```

Setting a credit limit is optional but recommended — it bounds cost on long multi-agent runs. In the Copilot app, workflows are available with no setup.

## Monitoring and resuming

- **CLI:** `/workflows` lists runs — `P` pauses, `X` cancels, `R` resumes.
- **App:** the **Workflows** button above the prompt box shows active, resumable, and finished runs.
- Resuming reuses saved results from completed steps instead of starting over. Canceled runs can't be resumed. Subagents inherit your session's permission grants.

## The release-check blueprint

See [`workflows/release-check.md`](../workflows/release-check.md): a complete, copy-paste authoring spec for a release-check workflow — deterministic checks, parallel agent assessment, structured findings, and a human checkpoint before release notes are drafted. Paste its authoring prompt into Copilot and you'll have a working workflow in minutes.
