# Managing Context Windows

Practical techniques for fitting more signal into limited context.

## 1. Summarize, don't paste

Paste the relevant function, not the whole file. If the model needs
broader context, ask it to request specific pieces: "tell me which
files you need to see."

## 2. Compress conversation history

When a chat gets long, ask: "summarize our decisions and open questions
so far, then continue." Start a fresh chat with the summary.

## 3. Reference by pointer

"See `src/token_estimator.py:estimate_tokens`" beats pasting the
function when the model already has repo access (agents, IDE assistants).

## 4. Strip the noise

Remove stack-trace frames from vendored code and minified bundles before
pasting. Keep the first frame in your own code plus the error line.

## 5. Budget before you build

Estimate tokens (see `src/token_estimator.py`) before sending large
prompts — truncate or chunk when over ~70% of the window so the model
keeps room to answer.
