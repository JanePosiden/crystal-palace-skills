---
name: clarify-then-brief
description: "PALACE bridge: Align → Explicit Brief → S-Filter → Build → Lean Handoff → Control-variable if stuck. Use for non-trivial Crystal Palace work. Triggers on clarify-then-brief, palace, 水晶宫, scope then brief."
---

# Clarify → Brief → Palace

Prefer the installed orchestrator: `.cursor/skills/palace-orchestrator/SKILL.md`.  
This file is the same pipeline for `skills-source/` readers.

```text
Align (grilling)
  → Explicit Brief (E)
  → Crystal Vault + S-Filter (P)
  → Grow from Arbor (A)
  → Build
  → Lean Handoff (L)
  → if stuck: Control-variable (C)
```

## Commands (repo root)

```bash
python crystal-palace/palace_cli.py init
python crystal-palace/palace_cli.py brief-init --predicate "<成功谓词>"
python crystal-palace/palace_cli.py s-filter --task "<派工描述>"
python crystal-palace/palace_cli.py handoff --intent "..." --delta "..." --artifacts "..." --next-steps "..." --task "..."
python crystal-palace/palace_cli.py reject --reason "..."
python crystal-palace/palace_cli.py self-test
```

- Phase 0: `grilling` until shared understanding; no coding  
- Phase 1: fill `crystal-palace/state/brief.md`  
- Phase 2: `s-filter` must not `BLOCK`; paste `relevant_s` verbatim  
- Phase 3: build with feedback; on reject×3 → `control-variable-tune`  
- Phase 4: `handoff` (auto S-Filter if needed)  

Related: `crystal-palace-memory` · `lean-handoff` · `control-variable-tune`
