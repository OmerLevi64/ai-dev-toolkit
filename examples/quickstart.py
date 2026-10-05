"""Runnable quickstart: estimate tokens and build a structured prompt."""

from src.prompt_builder import build_prompt
from src.token_estimator import estimate_tokens, truncate_to_tokens


def main() -> None:
    with open("prompts/code-assistant.md", encoding="utf-8") as f:
        template = f.read()

    print(f"Template is ~{estimate_tokens(template)} tokens")

    prompt = build_prompt(
        role="You are a senior Python reviewer.",
        task="Review the diff below for bugs and style issues.",
        context="Python 3.11, the codebase uses type hints throughout.",
        output_format="Return a bullet list: file, line, issue, suggestion.",
    )
    print(f"Built prompt is ~{estimate_tokens(prompt)} tokens")

    long_text = "lorem ipsum " * 1000
    print(f"Truncated sample: ~{estimate_tokens(truncate_to_tokens(long_text, 50))} tokens")


if __name__ == "__main__":
    main()
