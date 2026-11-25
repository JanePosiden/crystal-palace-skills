---
name: crystal-palace-memory
description: "Crystal Vault (S) and Arbor Anchors (A). Use when storing protected human/superior requirements, running S-Filter before dispatch, requesting S changes, or growing from confirmed structures. Triggers on crystal vault, S-Filter, S级, A级, 水晶宫, arbor, protected memory."
---

# Crystal Palace Memory

**P · Protected** + **A · Arbor**

## Hard rules

1. S verbatim is law. Never invent, paraphrase-as-memory, delete, or silently edit S.
2. Before every task dispatch / sub-agent spawn, run S-Filter.
3. To change S: `s-request-change` → superior `s-approve-change` only.
4. A conflicts with S → S wins.
5. Too many S → compress *display*; Vault files stay complete.

## CLI (run from repo root)

```bash
python crystal-palace/palace_cli.py init
python crystal-palace/palace_cli.py s-add --title "..." --verbatim "..." --tags "红线,安全"
python crystal-palace/palace_cli.py a-add --title "..." --verbatim "..."
python crystal-palace/palace_cli.py s-filter --task "本次要派的任务描述"
python crystal-palace/palace_cli.py show --id s-xxx
python crystal-palace/palace_cli.py s-request-change --target-id s-xxx --reason "..." --proposed "..."
python crystal-palace/palace_cli.py s-approve-change --id cr-xxx --note "approved"
python crystal-palace/palace_cli.py leaf-add --title "临时笔记" --body "..."
python crystal-palace/palace_cli.py list
python crystal-palace/palace_cli.py verify
python crystal-palace/palace_cli.py status
python crystal-palace/palace_cli.py demo
```

Filter report: `crystal-palace/state/last_s_filter.json`  
Include every `relevant_s[].verbatim` in the worker brief **unchanged**.

## Agent checklist

- [ ] `s-filter` run for this dispatch
- [ ] status not `BLOCK`
- [ ] relevant S pasted/pointed verbatim
- [ ] A anchors used as growth starting points
- [ ] no S mutation without pending→approved flow
