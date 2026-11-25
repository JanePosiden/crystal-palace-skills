# CLAUDE.md

<!-- BEGIN CRYSTAL PALACE -->
# Crystal Palace (PALACE)

This repo uses Crystal Palace — Protected · Arbor · Lean · Alignment · Control-variable · Explicit.

## Must follow

1. **S-tier (Crystal Vault)** in `crystal-palace/vault/S/` is immutable law. No inventing, paraphrasing-as-memory, deleting, or silent edits.
2. Before dispatching real work or Task/sub-agents, run:
   `python crystal-palace/palace_cli.py s-filter --task "<description>"`
   On `BLOCK`, stop.
3. S edits require `s-request-change` then human/superior `s-approve-change`.
4. Grow from **A** anchors in `vault/A/`; S overrides A on conflict.
5. Align (grill) before coding vague goals; write Explicit Brief for non-trivial work.
6. Session handoff via `palace_cli.py handoff` (lean, lossless).
7. Stuck / rejected ≥3 times → control-variable tune (one part per experiment).

## Skills directory

Installed under `.claude/skills/` (`palace-orchestrator`, `crystal-palace-memory`, `lean-handoff`, `control-variable-tune`). Load them when the task matches.

## Quick commands

```bash
python crystal-palace/palace_cli.py init
python crystal-palace/palace_cli.py s-filter --task "..."
python crystal-palace/palace_cli.py brief-init --predicate "..."
python crystal-palace/palace_cli.py handoff --intent "..." --delta "..." --task "..."
python crystal-palace/palace_cli.py install --target all
python crystal-palace/palace_cli.py doctor
```
<!-- END CRYSTAL PALACE -->
