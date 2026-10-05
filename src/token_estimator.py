"""Rough token estimation for prompt text.

Uses the common "~4 characters per token" heuristic plus truncation
helpers. Good enough for budgeting and truncation decisions; for exact
counts, use the model provider's tokenizer.
"""

CHARS_PER_TOKEN = 4


def estimate_tokens(text: str) -> int:
    """Estimate the number of tokens in *text*."""
    if not text:
        return 0
    return max(1, len(text) // CHARS_PER_TOKEN)


def truncate_to_tokens(text: str, max_tokens: int) -> str:
    """Truncate *text* to roughly *max_tokens* tokens.

    Never expands short text; appends an ellipsis marker when truncated.
    """
    if max_tokens <= 0:
        return ""
    if estimate_tokens(text) <= max_tokens:
        return text
    return text[: max_tokens * CHARS_PER_TOKEN].rstrip() + "…"
