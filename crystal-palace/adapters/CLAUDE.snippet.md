<!-- BEGIN CRYSTAL PALACE -->
# Crystal Palace (PALACE)

Follow PALACE when doing non-trivial work in this repository.

## Hard rules

- Store human/superior hard requirements in `crystal-palace/vault/S/` via `palace_cli.py s-add` (**verbatim**). Never invent, paraphrase-as-memory, delete, or silently edit S.
- Before dispatching work or Task/sub-agents: `python crystal-palace/palace_cli.py s-filter --task "..."`. `BLOCK` → stop.
- Mutate S only through `s-request-change` → `s-approve-change`.
- Confirmed structures go in `vault/A/` (`a-add`). S overrides A on conflict.
- Vague goals: grill first. Write Explicit Brief (`brief-init`) before long runs.
- Handoffs: `palace_cli.py handoff` (do not replace S/A with summaries).
- Stuck / reject×3: control-variable tune — **one** changed part per experiment.

## Skills to load

`palace-orchestrator` · `crystal-palace-memory` · `lean-handoff` · `control-variable-tune`

## Quick commands

```bash
python crystal-palace/palace_cli.py init
python crystal-palace/palace_cli.py s-filter --task "..."
python crystal-palace/palace_cli.py handoff --intent "..." --task "..."
python crystal-palace/palace_cli.py self-test
```
<!-- END CRYSTAL PALACE -->
