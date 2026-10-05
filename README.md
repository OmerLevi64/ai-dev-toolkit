# AI Dev Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/OmerLevi64/ai-dev-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/OmerLevi64/ai-dev-toolkit/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
[![GitHub stars](https://img.shields.io/github/stars/OmerLevi64/ai-dev-toolkit?style=social)](https://github.com/OmerLevi64/ai-dev-toolkit/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/OmerLevi64/ai-dev-toolkit)](https://github.com/OmerLevi64/ai-dev-toolkit/commits/main)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

Practical toolkit for developers building with AI — curated prompt templates, Python utilities, and engineering guides.

## Features

- Curated prompt templates — battle-tested system prompts for coding assistance, code review, debugging, and refactoring (`prompts/`)
- Python utilities — token estimation and structured prompt building (`src/`)
- Engineering guides — practical prompt-engineering techniques for developers (`guides/`)

## Quick start

```bash
git clone https://github.com/OmerLevi64/ai-dev-toolkit.git
cd ai-dev-toolkit
```

Estimate tokens before sending a prompt to an API:

```python
from src.token_estimator import estimate_tokens

text = open("prompts/code-assistant.md").read()
print(estimate_tokens(text), "tokens (approx.)")
```

Build a structured prompt:

```python
from src.prompt_builder import build_prompt

prompt = build_prompt(
    role="You are a senior Python reviewer.",
    task="Review the diff below for bugs and style issues.",
    context="Python 3.11, the codebase uses type hints throughout.",
    output_format="Return a bullet list: file, line, issue, suggestion.",
)
print(prompt)
```

## Project structure

```
ai-dev-toolkit/
├── prompts/                 # Reusable prompt templates for dev workflows
├── guides/                  # Short, practical engineering guides
├── src/                     # Python utilities
├── tests/                   # Smoke tests (run in CI)
└── .github/workflows/       # CI workflow
```

## Prompts

| Template | Use it for |
|---|---|
| `prompts/code-assistant.md` | General-purpose coding assistant system prompt |
| `prompts/code-review.md` | Structured code review system prompt |

## Guides

- `guides/prompt-engineering-basics.md` — core techniques: roles, constraints, examples, output formats

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

## License

MIT — see [LICENSE](LICENSE).
