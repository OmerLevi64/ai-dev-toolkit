"""Smoke tests for the toolkit utilities."""

from src.prompt_builder import build_prompt
from src.token_estimator import estimate_tokens, truncate_to_tokens


def test_estimate_tokens_empty():
    assert estimate_tokens("") == 0


def test_estimate_tokens_heuristic():
    # 11 chars at ~4 chars/token
    assert estimate_tokens("hello world") == 2


def test_truncate_keeps_short_text():
    assert truncate_to_tokens("short", 100) == "short"


def test_truncate_limits_long_text():
    text = "x" * 1000
    truncated = truncate_to_tokens(text, 10)
    assert estimate_tokens(truncated) <= 11  # heuristic + ellipsis slack


def test_build_prompt_skips_empty_sections():
    prompt = build_prompt(role="Reviewer", task="Review this.")
    assert "## Role" in prompt
    assert "## Task" in prompt
    assert "## Context" not in prompt


def test_build_prompt_empty():
    assert build_prompt() == ""
