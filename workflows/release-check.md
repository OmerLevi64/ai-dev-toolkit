# Release Check — Dynamic Workflow Blueprint

A ready-to-use specification for a `release-check` dynamic workflow: it verifies a release is actually ready, has agents assess anything suspicious in parallel, then **pauses for a human** before drafting release notes.

Don't hand-write the extension code — paste the authoring prompt below into a Copilot session (Copilot app, or CLI with `--experimental`) and Copilot will author and register the workflow for you.

## The authoring prompt

```text
Create a dynamic workflow named release-check that verifies whether a
software release is ready, with an AI credit limit of 300.

Inputs: version (string, e.g. "0.3.0"), repo_path (string, defaults to
the current directory).

Stage 1 — gather (code, sequential):
- List commits and changed files since the previous git tag.
- Read the CHANGELOG and check it has an entry for the target version.

Stage 2 — deterministic checks (code, parallel):
- Check the version was bumped to the target version in the package
  metadata (detect which exists: src/__init__.py, package.json, or
  pyproject.toml).
- Run the test suite and record pass/fail per test file.

Stage 3 — agent assessment (two agents, parallel):
- Agent A: assess any test failures — real regressions or
  flaky/environmental? Return a structured verdict per failure.
- Agent B: review the diff since the last tag for risky changes
  (migrations, API breaks, security-sensitive code). Return findings
  as a structured list with severity.

Stage 4 — checkpoint:
- Combine all findings into a single structured release-readiness
  report and PAUSE for human review. Do not proceed until resumed.

Stage 5 — on resume:
- Draft release notes from the CHANGELOG entry and the commit list,
  grouped under Added / Changed / Fixed.
- Return the report and the draft notes as the workflow result.
```

## Why it's shaped this way

- **Code does the deterministic parts** (git, file checks, test runs) — no need to spend agent judgment on what a script can answer.
- **Agents do the judgment parts** (are failures real? is the diff risky?) — in parallel, since they don't depend on each other.
- **Structured results** flow from each stage into the report, so the checkpoint shows evidence, not vibes.
- **The checkpoint is the point**: release decisions stay human. The workflow prepares everything; you make the call.

## Running it

```text
Run the release-check dynamic workflow for version 0.3.0.
```

```bash
copilot workflow run release-check \
  --args '{"version":"0.3.0"}' \
  --allow-tool=read
```

## Sharing it with the repo

After Copilot authors it, ask for its extension path (*"Tell me the path to the release-check dynamic workflow"*), then copy that directory into this repo's `.github/extensions/` so the whole team gets it. Commit the directory like any other project file.

## Customizing

- Add a third agent to check docs coverage, or a code step that lints commit messages.
- Raise the credit limit for large repos; lower it when testing. GitHub's own advice: test small first (2–3 files), then scale.
