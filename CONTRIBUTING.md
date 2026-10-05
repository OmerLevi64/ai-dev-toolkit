# Contributing to AI Dev Toolkit

Thanks for considering a contribution! This document keeps the process smooth.

## How to contribute

1. **Fork** the repository and create a branch from `main`:
   `git checkout -b feature/my-improvement`
2. Make your change. Keep it focused — one concern per pull request.
3. Add or update tests under `tests/` if your change touches `src/`.
4. Make sure CI passes (`python -m pytest -q` locally).
5. Open a pull request with a clear title and a short description of the
   **what** and the **why**.

## Prompt templates

New templates go in `prompts/` as Markdown files with:

- A `# Title` and one-line description of when to use it
- The prompt itself in a fenced block (or as the document body)
- A short "tips" section if the template has non-obvious knobs

## Guides

Guides go in `guides/` and should be practical and concise: teach one
technique, show a before/after example, keep it under ~150 lines.

## Code style

- Python 3.10+, type hints on public functions, docstrings everywhere.
- Keep utilities dependency-free so the toolkit stays easy to adopt.

## Code of conduct

Be kind and constructive. Assume good intent.
