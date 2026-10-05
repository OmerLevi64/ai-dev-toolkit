# Prompt Engineering Basics for Developers

Short, practical techniques that reliably improve AI output on coding tasks.

## 1. Assign a role

Roles set the vocabulary and standards of the answer.

Instead of "Explain this code." try "You are a senior Python engineer.
Explain this code, flagging any concurrency risks."

## 2. Constrain the output format

Models follow explicit format instructions well.

Instead of "Review my diff." try "Review my diff. Return a bullet list:
file, line, issue, suggested fix. Skip style nits."

## 3. Give one example

A single input/output example beats paragraphs of description for
formatting tasks ("few-shot").

## 4. Provide context, not just the question

Include: language + version, framework, relevant existing code, and what
you already tried. The model cannot see your repo.

## 5. Decompose big tasks

"Refactor this module" becomes "1) list the responsibilities in this
module, 2) propose new boundaries, 3) refactor one boundary at a time."

## 6. Ask for verification hooks

End with "list your assumptions" or "what would you test to verify
this?" — it surfaces hallucinations before they reach production.

## 7. Iterate, don't restart

When output is close but off, say what to keep and what to change:
"Keep the structure, but use async/await instead of threads." Iterative
refinement converges faster than re-prompting from scratch.
