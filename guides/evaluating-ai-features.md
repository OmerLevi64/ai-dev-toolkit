# Evaluating AI Features

How to test features that call an LLM without going insane.

## 1. Separate the deterministic from the probabilistic

Test everything around the model call with normal unit tests: prompt
assembly, parsing, retries, fallbacks. Only the model's judgment itself
needs eval-style testing.

## 2. Golden examples

Keep a small set of input/output pairs. Re-run on every prompt change.
A 20-example set catches most regressions.

## 3. Assert on structure, sample on quality

Assert programmatically: valid JSON, required fields, length bounds.
Judge quality by sampling: review 10-20 outputs by eye per change.

## 4. Version your prompts

Treat prompts like code: keep them in files (see `prompts/`), review
changes in PRs, and note which model version each was tuned against.

## 5. Log production traffic

Sample real inputs/outputs (with privacy in mind). Today's edge case is
tomorrow's golden example.
