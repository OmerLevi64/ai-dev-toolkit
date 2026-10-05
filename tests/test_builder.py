"""Tests for the prompt builder utility."""

from src.prompt_builder import build_prompt


def test_all_sections():
    prompt = build_prompt(
        role="r", task="t", context="c", examples="e", output_format="o"
    )
    for heading in ("Role", "Task", "Context", "Examples", "Output format"):
        assert f"## {heading}" in prompt


def test_section_order():
    prompt = build_prompt(task="t", role="r")
    assert prompt.index("## Role") < prompt.index("## Task")


def test_examples_only():
    prompt = build_prompt(examples="in -> out")
    assert prompt == "## Examples\nin -> out"
