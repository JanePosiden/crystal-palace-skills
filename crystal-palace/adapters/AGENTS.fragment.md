<!-- BEGIN CRYSTAL PALACE -->
# Crystal Palace (PALACE)

Codex: load skills `palace-orchestrator`, `crystal-palace-memory`, `lean-handoff`, `control-variable-tune` from `.agents/skills/`.

## Runtime

```bash
python crystal-palace/palace_cli.py init
python crystal-palace/palace_cli.py s-filter --task "<dispatch>"
```

## Hard rules

1. **S Vault** — hard requirements/PII verbatim in `crystal-palace/vault/S/`. No invent / paraphrase-as-memory / silent edit. Change only via `s-request-change` → `s-approve-change`.
2. **S-Filter** before substantive dispatch; `BLOCK` ⇒ stop.
3. **A Arbor** — grow from `vault/A/`; S wins on conflict.
4. Vague goals → grill first; need Explicit Brief (`brief-init`) for non-trivial work.
5. Handoffs via `handoff` (keep S/A verbatim).
6. Stuck / reject×3 → one-variable tune (`tune-start` → `tune-score` → `tune-decide`).

Pipeline: Align → Brief → S-Filter → Build → Handoff → (Tune).
<!-- END CRYSTAL PALACE -->
