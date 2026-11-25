# Crystal Palace Rules (PALACE)

Follow PALACE when doing non-trivial work in this repository.

## Protected (S)

- Hard requirements and personal info from the human/superior belong in `crystal-palace/vault/S/` via:
  `python crystal-palace/palace_cli.py s-add ...`
- **Never** invent, paraphrase-as-memory, delete, or silently edit S verbatim.
- Before dispatching substantive work or sub-agents, run:
  `python crystal-palace/palace_cli.py s-filter --task "..."`
- To change S: `s-request-change` then wait for `s-approve-change`. Do not overwrite.

## Arbor (A)

- Confirmed structures/recipes go in `vault/A/` (`a-add`). Grow from A; do not reinvent when an A anchor fits.
- If A conflicts with S, **S wins**.

## Alignment

- Vague goals: grill first. Do not code until shared understanding or an Explicit Brief exists.

## Explicit

- Non-trivial work needs a success predicate and DOES NOT COUNT:
  `python crystal-palace/palace_cli.py brief-init --predicate "..."`

## Lean handoff

- Session handoffs use `palace_cli.py handoff` (or `lean-handoff` skill). Keep S/A verbatim; do not replace with vibes.

## Control-variable

- After repeated failures (rejection count ≥ 3 or user says stuck), change **one** factor per experiment via `tune-start` → `tune-score` → `tune-decide`.

## Entry skill

Prefer `palace-orchestrator` for end-to-end flow.
