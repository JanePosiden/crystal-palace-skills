# Crystal Palace package

Mature Agent Skill package for **Cursor · Claude Code · Codex · Grok(instructions)**.

## Layout

```text
crystal-palace/
├── palace_cli.py           # runtime (Vault, S-Filter, Brief, Handoff, Tune)
├── install_adapters.py     # multi-agent installer
├── skills/                 # canonical SKILL.md sources (+ agents/openai.yaml)
├── adapters/               # CLAUDE / AGENTS / Grok fragments + portable rule
├── vault/                  # S / A / leaves / pending / audit
└── state/                  # brief, handoff, filter, tune logs
```

## Install

```bash
# everything into this repo
python crystal-palace/install_adapters.py --target all

# or via CLI
python crystal-palace/palace_cli.py install --target all

# single target
python crystal-palace/install_adapters.py --target claude
python crystal-palace/install_adapters.py --target codex
python crystal-palace/install_adapters.py --target cursor

# user-global (Claude / Codex home dirs)
python crystal-palace/install_adapters.py --target claude --scope user
python crystal-palace/install_adapters.py --target codex --scope user
```

| Target | Skills land in | Rules / guidance |
|--------|----------------|------------------|
| Cursor | `.cursor/skills/` | `.cursor/rules/crystal-palace.mdc` |
| Claude | `.claude/skills/` | `CLAUDE.md` + `.claude/rules/` |
| Codex  | `.agents/skills/` | `AGENTS.md` |
| Grok   | (no skill host) | `GROK_CUSTOM_INSTRUCTIONS.md` to paste |

## Skills

| Skill | Role |
|-------|------|
| `palace-orchestrator` | End-to-end PALACE conductor |
| `crystal-palace-memory` | S/A vault + S-Filter |
| `lean-handoff` | Lossless handoff |
| `control-variable-tune` | One-factor convergence |

## Uninstall

```bash
python crystal-palace/palace_cli.py install --target all --uninstall
```

## Smoke test

```bash
python crystal-palace/palace_cli.py doctor
python crystal-palace/palace_cli.py self-test
python crystal-palace/palace_cli.py demo
```

## Maturity checklist

- [x] Canonical `skills/*/SKILL.md` + `agents/openai.yaml`
- [x] Runtime CLI with vault integrity + self-test
- [x] Adapters for Cursor / Claude / Codex / Grok
- [x] `install` / `uninstall` / `doctor`
- [x] Marked guidance blocks (idempotent upsert)
- [x] PACKAGE + INSTALL docs
