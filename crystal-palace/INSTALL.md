# Install Crystal Palace (mature skill package)

One package → **Cursor · Claude Code · Codex · Grok**.

## One command

```bash
# From the repo that contains crystal-palace/
python crystal-palace/palace_cli.py install --target all
python crystal-palace/palace_cli.py doctor
```

Or:

```bash
python crystal-palace/install_adapters.py --target all
```

## Per platform

| Target | Command | Lands in |
|--------|---------|----------|
| Cursor | `--target cursor` | `.cursor/skills/` + `.cursor/rules/crystal-palace.mdc` |
| Claude Code | `--target claude` | `.claude/skills/` + `CLAUDE.md` + `.claude/rules/` |
| Codex | `--target codex` | `.agents/skills/` + `AGENTS.md` |
| Grok | `--target grok` | `GROK.md`（粘贴到自定义指令） |

```bash
python crystal-palace/palace_cli.py install --target claude
python crystal-palace/palace_cli.py install --target codex
python crystal-palace/palace_cli.py install --target cursor
python crystal-palace/palace_cli.py install --target grok
```

### User-global (all repos)

```bash
python crystal-palace/palace_cli.py install --target claude --scope user
python crystal-palace/palace_cli.py install --target codex --scope user
python crystal-palace/palace_cli.py install --target cursor --scope user
```

### Uninstall

```bash
python crystal-palace/install_adapters.py --target all --uninstall
```

## After install

```bash
python crystal-palace/palace_cli.py init
python crystal-palace/palace_cli.py self-test
python crystal-palace/palace_cli.py demo
```

- **Claude Code**：打开本仓库即可；硬规则在 `CLAUDE.md`  
- **Codex**：硬规则在 `AGENTS.md`；skills 在 `.agents/skills/`  
- **Cursor**：已有 always-on rule + skills  
- **Grok**：把仓库根目录 `GROK.md` 粘进自定义指令；或在 Cursor 里直接选 Grok 模型（沿用 Cursor skills）

## Package layout

See [PACKAGE.md](./PACKAGE.md). Canonical skills live in `crystal-palace/skills/` — installer copies them out; edit there, then re-run `install`.
