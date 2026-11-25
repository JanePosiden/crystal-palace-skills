---
name: lean-handoff
description: "Lean lossless handoff for Crystal Palace. Use when compressing a session for the next agent, writing handoff docs, or context is full. Triggers on lean handoff, 保真交接, handoff, 上下文交接."
---

# Lean Handoff (L)

Produce a short, readable handoff that does **not** paraphrase Crystal Vault S entries.

## Procedure

1. Run (or reuse) S-Filter for the continuing task:
   ```bash
   python crystal-palace/palace_cli.py s-filter --task "<next session focus>"
   ```
2. Generate handoff:
   ```bash
   python crystal-palace/palace_cli.py handoff --intent "..." --delta "..." --artifacts "..." --next-steps "..." --decisions "..." --task "..."
   ```
   If `--task` is set (or no prior filter exists), handoff auto-runs S-Filter.
3. Outputs:
   - `crystal-palace/state/handoff.md`
   - a copy under the OS temp directory
   - `crystal-palace/state/last_s_filter.json`

## Required sections

S-Filter Result · Session Intent · Success Predicate · Does Not Count · A-Anchors · Decisions · Artifacts (paths verbatim) · Delta · Current State · Next Steps · Suggested Skills · Open Questions

## Rules

- Prefer pointers + short Delta over dumping chat history.
- S/A bodies stay verbatim quotes or file paths — never “summarized memory”.
- If Open Questions exist → grill before guessing; do not invent answers.
