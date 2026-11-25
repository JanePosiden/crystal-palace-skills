---
name: control-variable-tune
description: "Control-variable convergence when deliverables keep failing approval or prompt thrashing starts. Change one part at a time, score, keep/rollback/promote. Triggers on control-variable, 控制变量, tune, 调优, 卡死, rejection loop."
---

# Control-Variable Tune (C)

Lab, not casino. **One changed part per experiment.**

## When to start

- Superior rejection count ≥ 3 (`palace_cli.py reject`), or
- User says the work is stuck / thrashing prompts, or
- Scores flat across retries

## Algorithm

1. **Factorize** the prompt/solution into named parts (e.g. `role,constraints,tools,examples,output-contract`).
2. **Pick exactly one** `changed_part`. Lock the rest.
3. Write a **hypothesis**: which failure mode should improve.
4. Apply the minimal change; keep artifacts diffable.
5. Score against Success Predicate + relevant S (same rubric every round).
6. **Decide**:
   - `keep` — accept change; reset rejection counter
   - `rollback` — revert; try another single factor
   - `promote-a` — write confirmed structure into Arbor (**requires** `--title` + `--verbatim`)
   - `request-s` — only via S change-request flow

## CLI

```bash
python crystal-palace/palace_cli.py reject --reason "未达成功谓词"
# after 3 rejects, CLI exits 4 → start tune

python crystal-palace/palace_cli.py tune-start \
  --parts "role,constraints,examples,output-contract" \
  --changed-part "constraints" \
  --hypothesis "收紧约束会减少越界" \
  --change-summary "加一条禁止释义 S" \
  --baseline 6.0

python crystal-palace/palace_cli.py tune-score --score 8.5
python crystal-palace/palace_cli.py tune-decide --decision keep --note "improved"

# Or promote a confirmed recipe into Arbor:
python crystal-palace/palace_cli.py tune-decide --decision promote-a \
  --title "输出契约在前" \
  --verbatim "先锁定 output-contract，再补 examples。" \
  --note "stabilize"
```

State: `crystal-palace/state/tune_log.json`

## Forbidden

- Changing multiple parts in one experiment
- Promoting to S without approval flow
- Closing without a numeric score
- `promote-a` without writing the confirmed structure (`--title`/`--verbatim`)
