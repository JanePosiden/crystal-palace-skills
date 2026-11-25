# Crystal Palace

Mature **PALACE** skill pack + runnable runtime for Cursor, Claude Code, Codex, and portable Grok prompts.

**PALACE** = Protected · Arbor · Lean · Alignment · Control-variable · Explicit

## Install (one command)

From the **repository root**:

```bash
# All adapters (Cursor + Claude + Codex + Grok pack)
python crystal-palace/palace_cli.py install --target all

# Or individually
python crystal-palace/palace_cli.py install --target cursor
python crystal-palace/palace_cli.py install --target claude
python crystal-palace/palace_cli.py install --target codex
python crystal-palace/palace_cli.py install --target grok

# User-global skills (every repo on this machine)
python crystal-palace/palace_cli.py install --target all --user

# Preview
python crystal-palace/palace_cli.py install --target all --dry-run
```

Equivalent:

```bash
python crystal-palace/install_adapters.py --target all
```

### What gets installed

| Target | Skills | Hard rules / guide |
|--------|--------|--------------------|
| **Cursor** | `.cursor/skills/<name>/` | `.cursor/rules/crystal-palace.mdc` |
| **Claude Code** | `.claude/skills/<name>/` | `CLAUDE.md` block + `.claude/rules/crystal-palace.md` |
| **Codex** | `.agents/skills/<name>/` | `AGENTS.md` block |
| **Grok** | — | `adapters/GROK_SYSTEM_PROMPT.md` (paste into custom instructions) |

Canonical skill source: `crystal-palace/skills/`  
(installer copies outward — edit here, then re-run install)

## Skills in this pack

| Skill | Role |
|-------|------|
| `palace-orchestrator` | End-to-end conductor |
| `crystal-palace-memory` | Vault S/A + S-Filter |
| `lean-handoff` | Lossless handoff |
| `control-variable-tune` | One-factor tuning loop |

## Runtime CLI

```bash
python crystal-palace/palace_cli.py init
python crystal-palace/palace_cli.py self-test
python crystal-palace/palace_cli.py demo
python crystal-palace/palace_cli.py status
```

| Command | Purpose |
|---------|---------|
| `s-add` / `a-add` / `show` / `list` / `verify` | Memory CRUD + integrity |
| `s-filter --task "..."` | Dispatch gate (`BLOCK` → exit 3) |
| `s-request-change` / `s-approve-change` | Controlled S mutation |
| `brief-init` | Explicit Brief scaffold |
| `handoff` | Lean handoff (auto S-Filter) |
| `reject` / `tune-start` / `tune-score` / `tune-decide` | Control-variable loop |
| `leaf-add` | Compressible session foliage |
| `install --target …` | Multi-agent adapters |

## Layout

```text
crystal-palace/
├── palace_cli.py              # runtime
├── install_adapters.py        # Cursor/Claude/Codex/Grok installer
├── skills/                    # canonical SKILL.md pack
├── adapters/                  # rules + AGENTS/CLAUDE/GROK snippets
├── vault/                     # S / A / leaves / pending / audit
└── state/                     # brief, handoff, filter, tune logs
```

## After install — smoke check

```bash
python crystal-palace/palace_cli.py self-test
python crystal-palace/palace_cli.py s-filter --task "继续当前工作"
```

Then in Claude Code / Codex / Cursor, ask: **「按 Crystal Palace / PALACE 流程推进」**.
