"""Build structured prompts from reusable sections.

Structured prompts (role, task, context, examples, output format) are
easier to version, review, and A/B test than free-form strings.
"""


def build_prompt(
    role: str = "",
    task: str = "",
    context: str = "",
    examples: str = "",
    output_format: str = "",
) -> str:
    """Assemble a prompt from named sections, skipping empty ones."""
    sections = []
    if role:
        sections.append(f"## Role\n{role}")
    if task:
        sections.append(f"## Task\n{task}")
    if context:
        sections.append(f"## Context\n{context}")
    if examples:
        sections.append(f"## Examples\n{examples}")
    if output_format:
        sections.append(f"## Output format\n{output_format}")
    return "\n\n".join(sections)
