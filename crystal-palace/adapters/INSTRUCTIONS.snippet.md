<!-- BEGIN CRYSTAL PALACE -->
# Crystal Palace (PALACE)

This repository uses **Crystal Palace** — Protected · Arbor · Lean · Alignment · Control-variable · Explicit.

## Runtime

From the repo root (directory that contains `crystal-palace/`):

```bash
python crystal-palace/palace_cli.py init
python crystal-palace/palace_cli.py status
python crystal-palace/palace_cli.py s-filter --task "<dispatch>"
```

If `PALACE_HOME` is set, use `python "$PALACE_HOME/palace_cli.py"` instead.

## Hard rules

1. **S (Crystal Vault)** — human/superior hard requirements & personal info are verbatim in `crystal-palace/vault/S/`. Never invent, paraphrase-as-memory, delete, or silently edit. Change only via `s-request-change` → `s-approve-change`.
2. **S-Filter** — before substantive dispatch / sub-agents, run `s-filter`. `BLOCK` ⇒ stop.
3. **A (Arbor)** — grow from confirmed structures in `vault/A/`. S wins over A on conflict.
4. **Alignment** — vague goals: grill first; no coding until shared understanding or Explicit Brief.
5. **Explicit Brief** — non-trivial work needs success predicate + DOES NOT COUNT (`brief-init`).
6. **Lean handoff** — use `handoff`; keep S/A verbatim.
7. **Control-variable** — after reject×3 or stuck: change **one** factor (`tune-start` → `tune-score` → `tune-decide`).

## Skills to load

- `palace-orchestrator` — end-to-end conductor
- `crystal-palace-memory` — Vault + S-Filter
- `lean-handoff` — lossless handoff
- `control-variable-tune` — one-variable experiments

Pipeline: Align → Explicit Brief → S-Filter → Build → Lean Handoff → (if stuck) Control-variable.
<!-- END CRYSTAL PALACE -->
