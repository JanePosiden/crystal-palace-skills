<!-- BEGIN CRYSTAL PALACE -->
# Crystal Palace (PALACE)

This repo uses **Crystal Palace** for human–agent collaboration.

## Hard rules

- **S (Crystal Vault)**: human/superior hard requirements & personal info live in `crystal-palace/vault/S/` as verbatim text. Never invent, paraphrase-as-memory, delete, or silently edit S.
- **Before dispatch / sub-agents**: run `python crystal-palace/palace_cli.py s-filter --task "..."`. If status is `BLOCK`, stop.
- **Change S**: only via `s-request-change` → superior `s-approve-change`.
- **A (Arbor)**: confirmed structures/recipes in `vault/A/`. Grow from A; if A conflicts with S, **S wins**.
- **Alignment**: vague goals → grill first; no coding until shared understanding or Explicit Brief.
- **Explicit**: non-trivial work needs success predicate + DOES NOT COUNT (`brief-init` / `state/brief.md`).
- **Lean handoff**: `palace_cli.py handoff` — keep S/A verbatim.
- **Control-variable**: after reject×3 or stuck, change **one** factor per experiment (`tune-start` → `tune-score` → `tune-decide`).

## Skills

Use when relevant: `palace-orchestrator`, `crystal-palace-memory`, `lean-handoff`, `control-variable-tune`.

## CLI

```bash
python crystal-palace/palace_cli.py status
python crystal-palace/palace_cli.py s-filter --task "<dispatch>"
python crystal-palace/palace_cli.py self-test
```
<!-- END CRYSTAL PALACE -->
