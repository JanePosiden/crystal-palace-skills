---
name: palace-orchestrator
description: "Crystal Palace end-to-end orchestrator: Align → Explicit Brief → S-Filter → Build → Lean Handoff → Control-variable if stuck. Use for non-trivial work under PALACE. Triggers on palace, crystal palace, PALACE, 水晶宫流水线, clarify-then-brief."
---

# Palace Orchestrator

End-to-end PALACE flow. Load specialized skills as needed; keep this file as the conductor.

```text
Align (grilling)
  → Explicit Brief (E)
  → Crystal Vault + S-Filter (P)
  → Grow from Arbor (A)
  → Build with feedback
  → Lean Handoff (L)
  → if stuck: Control-variable (C)
```

## Phase 0 — Align

If shared understanding is missing, run `grilling` / `grill-me`:

- Design tree; ask only the frontier each round
- Facts via tools/sub-agents; decisions from the human
- Stop when frontier empty + user confirms
- **No coding / no long-run launch in this phase**

Candidate hard requirements → propose `s-add` (human confirms verbatim).

## Phase 1 — Explicit Brief (E)

```bash
python crystal-palace/palace_cli.py brief-init --predicate "<一句成功谓词>"
```

Fill `crystal-palace/state/brief.md`: DEFINITIONS · TASK · DOES NOT COUNT · CONTRACTS · VERIFICATION · RETURN CONDITION.

Red-team: cheapest fake-done → add to DOES NOT COUNT.  
If predicate cannot be written → back to Phase 0.

## Phase 2 — Remember + S-Filter (P/A)

```bash
python crystal-palace/palace_cli.py s-filter --task "<dispatch text>"
```

- `BLOCK` → stop; escalate
- Paste `relevant_s` verbatim into the worker brief
- Prefer A anchors as structural starting points

## Phase 3 — Build

Implement against the brief. Prefer feedback loops (`tdd`, review).  
On superior rejection:

```bash
python crystal-palace/palace_cli.py reject --reason "..."
```

Exit code 4 ⇒ start `control-variable-tune`.

## Phase 4 — Lean Handoff (L)

```bash
python crystal-palace/palace_cli.py handoff --intent "..." --delta "..." --artifacts "..." --next-steps "..."
```

## Phase 5 — Stop

Only when RETURN CONDITION holds. Status reports listed under DOES NOT COUNT do not count.

## Related skills

`crystal-palace-memory` · `lean-handoff` · `control-variable-tune` · `grilling` · `long-horizon-prompting`
