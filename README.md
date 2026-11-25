# Crystal Palace

## 人机协作的最终形态。

**PALACE** — *Protected · Arbor · Lean · Alignment · Control-variable · Explicit*

> 把「跟 Agent 干活」从玄学聊天，升级成可对齐、可记忆、可交接、可早停调优的协作操作系统（Collaboration OS for Agents）。

一句话：**S 级进水晶宫永不丢，A 级长成树，先拷问再动手，卡死了用控制变量打磨到收敛。**

————————————————————————

## PALACE 六字母定义


| 字母    | 全称                           | 含义                                                                                                     |
| ----- | ---------------------------- | ------------------------------------------------------------------------------------------------------ |
| **P** | **Protected**（受保护根主权）        | 真人/上级的硬要求与个人信息写入 **Crystal Vault（S 级）**。原文 verbatim；禁编撰、删除、遗忘、幻觉。每次派工必须过 **S-Filter**。要改？请示上级，评估通过才能动。 |
| **A** | **Arbor**（树状权威锚定）            | 已确认的目录、结构、配方进入 **Arbor Anchors（A 级）**。确认后尽量沿此分叉生长——S 是根，A 是枝，会话细节是叶。叶子可落，树干不焚。                         |
| **L** | **Lean**（无损耗交接）              | 上下文压缩要短、要可读，更要原汁原味。Handoff = 分区指针 + Delta，不是空话状态报告。败者细节可归档；根级约束永不被摘要偷换。                                |
| **A** | **Alignment**（对齐优先）          | 动手前先 **grilling**：设计树 + frontier 轮询，问到共享理解。事实 Agent 查，决策人拍板。对齐失败是第一事故源——PALACE 从根上切掉。                  |
| **C** | **Control-variable**（控制变量收敛） | 交付连否、提示词玄学连改时启用：拆部件 → **一次只动一个变量** → 前瞻预期 → 同款评审打分 → 回滚或固化进 A/S。实验室，不是赌场。                              |
| **E** | **Explicit**（显式工程任务书）        | 成功谓词、DOES NOT COUNT、handoff contract、审计门、努力下限。写不出谓词就别 launch。完成标准是对产物的判定，不是「我觉得差不多了」。                  |


扳机纪律：

- **S 过多**：压缩展示层可以，Vault 原文必须在。  
- **A 与 S 冲突**：S 赢。  
- **反复不达标**：进 Control-variable 环，禁止一次拧五个旋钮。

————————————————————————

## 为什么用 Crystal Palace

普通 Agent 协作会陷入五件事：


| 痛点        | 人话             | 后果                        |
| --------- | -------------- | ------------------------- |
| **对齐漂移**  | 没问清楚就开写        | 返工、推倒重来、信任崩塌              |
| **根记忆蒸发** | 压缩/换会话后硬要求消失   | 隐私泄露风险、上级红线被踩、同一句话重复十次    |
| **摘要偷换**  | 「大概记得」代替原文     | 幻觉寄生、约束变软、前后打架            |
| **交接失真**  | handoff 变成散文日记 | 下一棒考古聊天记录，Token 双倍烧       |
| **提示词内卷** | 卡死就整段重写提示词     | 无法归因、Model Collapse 式越改越飘 |


Crystal Palace 用工程范式一把收束：


| 包装名                       | 含义                    |
| ------------------------- | --------------------- |
| **Crystal Vault（S）**      | 根级记忆主权；派工过滤器；修改走请示    |
| **Arbor Growth（A）**       | 已确认结构当树干，禁止每次焚林开荒     |
| **Grilling Alignment**    | 拷问式访谈清空设计树再动手         |
| **Explicit Brief**        | 伪形式任务书：谓词 + 近失清单 + 契约 |
| **Lean Lossless Handoff** | 精悍分区交接；S/A 指针回 Vault  |
| **Control-Variable Loop** | 卡住时最小改动、可审计收敛         |
| **Feedback Build**        | TDD / 诊断 / 双轴评审——盲飞出局 |


不是「再堆一段 system prompt 碰运气」，而是 **在一份协作上把质量与记忆打磨到可交接、可收敛** ——少遗忘、少幻觉、多可审计增量。

**Crystal 不只在「更华丽的隐喻」，而在：更硬的记忆主权 + 更狠的对齐门禁 + 更瘦的交接上下文 + 更科学的调参环。**

————————————————————————

## 痛点 → 解法（对照表）


| #   | 你正在受的罪          | 没有 PALACE       | 有 Crystal Palace                    |
| --- | --------------- | --------------- | ----------------------------------- |
| 1   | Agent 做的不是我想要的  | 靠运气重说需求         | **Alignment**：grill 到 frontier 空再动手 |
| 2   | 「上次不是说了吗」       | 聊天记录里翻；一压缩就没    | **Protected**：S 进水晶宫；派工必过 S-Filter  |
| 3   | 换个窗口 Agent 失忆   | 从头复述 preference | **Arbor**：A 级结构续命；叶子可剪根不朽           |
| 4   | 交接后下一棒开摆        | 散文摘要，细节全丢       | **Lean**：分区 handoff + 产物路径 verbatim |
| 5   | 改了八版提示词仍不达标     | 一次改五处，无法归因      | **Control-variable**：一变量一实验，可回滚     |
| 6   | 长跑跑出「看起来完成了」    | 近失版本蒙混过关        | **Explicit**：DOES NOT COUNT + 审计门   |
| 7   | 代码能跑但越来越烂       | 无反馈环 / 无架构投资    | **TDD · code-review · 架构勘察** 内建进流水线 |
| 8   | 多 Agent 互相改到死循环 | Token 焚烧炉       | **Brief 契约 + 评测/早停调优** 可熔断          |


————————————————————————

## 横向对比


| 维度     | 空聊 / Vibe Prompting | 巨型 System Prompt | 流程绑架框架（大而全） | **Crystal Palace · PALACE** |
| ------ | ------------------- | ---------------- | ----------- | --------------------------- |
| 对齐     | 你自己反复叮嘱             | 写进 prompt 希望它记得  | 接管全流程，你丢控制权 | **grilling 门禁**；瞬时对齐        |
| 记忆     | 窗口一满就丢              | 全塞进上下文 → 注意力稀释   | 黑盒状态        | **S/A/叶 分级**；Vault 落盘       |
| 修改权威要求 | Agent 随口「好的」就改      | 无审批              | 不明          | **请示 → 评估 → 写入**            |
| 完成标准   | 「差不多就行」             | 形容词堆砌            | 框架内置，难定制    | **成功谓词 + DOES NOT COUNT**   |
| 交接     | 复制聊天记录              | 再喂一遍长 prompt     | 绑定特定工具链     | **Lean handoff**；精悍 × 保真    |
| 卡死怎么办  | 换模型 / 重写全文          | 继续堆规则            | 跟框架对着干      | **控制变量环**；可归因收敛             |
| 可组合性   | 无                   | 差（一团）            | 差（绑定流程）     | **小 skill 可编排**；按需加载        |
| 可审计性   | 低                   | 低                | 中           | **高**：过滤器、契约、打分、回滚          |
| 人的控制权  | 表面有、实际无             | 表面有              | 被拿走         | **决策在人，执行在 Agent**          |


**一句话对比：**  
别人让你「会写提示词」；PALACE 让 Agent **不敢忘、不敢猜、不敢瞎改、卡死了会做实验。**

————————————————————————

## 能力疆域：一套 OS，多条战线

凡是需要 **对齐 → 记住 → 交付 → 交接 → 打磨** 的活，都能挂上同一条 PALACE 流水线：


| #   | 场景                     | Crystal Palace 怎么「宫殿级」                                                                         |
| --- | ---------------------- | ---------------------------------------------------------------------------------------------- |
| 1   | **写代码 / 工程交付**         | grill 需求 → explicit brief → S-Filter 派工 → tdd / implement / code-review → lean handoff；架构勘察防泥球 |
| 2   | **长跑 Agent / 多 Agent** | long-horizon 任务书 + 契约门；多 Agent 拓扑只在隔离上下文时启用；交接不靠电话游戏                                           |
| 3   | **提示词 / 人设调优**         | 控制变量拆部件；评审 Agent 对照 S+谓词打分；少量多次前瞻迭代                                                            |
| 4   | **产品文档与方案**            | 对齐词表 → 规格/工单 → DOES NOT COUNT 干掉空话方案 → 版本可交接                                                   |
| 5   | **日常职场文书**             | 周报/纪要/向上同步：先问清受众与成功标准，再写；交接给下一窗口不丢红线                                                           |
| 6   | **创意与文案打磨**            | 对齐调性（S）→ A 级结构配方 → 卡住用控制变量改单一段落策略                                                              |
| 7   | **教研 / 面试 / 知识资产**     | teach + research + 共享语言；硬约束进 Vault，避免幻觉进教材                                                     |
| 8   | **合规 / 隐私敏感协作**        | 个人信息进 S；禁摘要冒充原文；派工过滤器当合规闸门                                                                     |


**价值主张：**  
一套 **Vault + Arbor + Grilling + Brief + Handoff + Control-variable**，横跨工程、文档、调优、日常与创意——把「会用 ChatGPT」抬成 **人机协作质量操作系统（Collaboration QC OS）**。

————————————————————————

## 架构一览

```text
┌─────────────────────────────────────────────────┐
│              Orchestrator / 主会话                 │
│     clarify-then-brief · S-Filter · early-stop    │
└───────────────────────┬─────────────────────────┘
                        │
     ┌──────────────────┼──────────────────┐
     ▼                  ▼                  ▼
┌─────────┐       ┌──────────┐       ┌────────────┐
│ Align   │       │ Crystal  │       │ Explicit   │
│ grilling│──────►│ Vault S  │◄──────│ Brief  E   │
└─────────┘       │ Arbor A  │       └────────────┘
                  └────┬─────┘
                       │ S-Filter
                       ▼
              ┌────────────────┐
              │ Build / Agents │  tdd · implement · review · multi-agent
              └────────┬───────┘
                       │
           ┌───────────┴───────────┐
           ▼                       ▼
    ┌─────────────┐         ┌─────────────────┐
    │ Lean Handoff│         │ Control-variable│  （连否 / 分数不涨时）
    │ L · compress│         │ C · 一变量一实验 │
    └─────────────┘         └─────────────────┘
```

设计取舍（文档可讲）：

- ❌ 不用「一个巨型 prompt 包打天下」——注意力会稀、根会丢  
- ❌ 不用「流程绑架、人失去控制」——决策必须在人  
- ❌ 不用「卡住就整段重写」——无法归因等于没调优  
- ✅ 用 **分级记忆 + 对齐门禁 + 显式任务书 + 可组合 skill + 控制变量收敛**

————————————————————————

## 核心卖点（对外用语）

可按需选用：

1. **Crystal Vault Sovereignty**（水晶宫主权记忆）
2. **S-Filter Dispatch Gate**（派工前根级过滤）
3. **Arbor Growth from Confirmed Structure**（从已确认结构长树）
4. **Alignment-First Grilling**（对齐优先拷问）
5. **Explicit Success Predicates & Non-Counting Outcomes**（显式成功谓词与近失清单）
6. **Lean Lossless Handoff**（精悍保真交接）
7. **Control-Variable Convergence Loop**（控制变量收敛环）
8. **Collaboration QC OS for Agents**（Agent 协作质量操作系统）

为什么「控制变量」高级且有用：  
许多团队最大问题是——提示词互改 → 分数不涨 → 越改越自嗨。  
PALACE 默认：**一次一个因子；抬不动就回滚；抬得动才写入 A/S。**  
优化越成功不应被玄学打断；**改不动才换因子，而不是换人生。**

————————————————————————

## Skills — 按工作流（全套能力）

需要时加载，不必一次塞进上下文。

### 1. Align — 问清楚


| Skill                                         | 做什么                 |
| --------------------------------------------- | ------------------- |
| `grill-me` / `grilling`                       | 无情拷问，设计树清空才罢休       |
| `grill-with-docs`                             | 拷问 + 词表 + ADR       |
| `domain-modeling`                             | 打磨领域语言              |
| `wait-what` / `to-questionnaire` / `ask-matt` | 听不懂重讲 · 问卷升级 · 流程路由 |


### 2. Specify — 可判定任务书


| Skill                                                | 做什么                      |
| ---------------------------------------------------- | ------------------------ |
| `clarify-then-brief`                                 | 对齐 → brief → 再实现/交接      |
| `long-horizon-prompting`                             | 长跑伪形式 brief：谓词、近失、契约、审计门 |
| `to-spec` / `to-tickets` / `wayfinder` / `prototype` | 规格 · 工单 · 超大规划 · 原型探路    |


### 3. Remember — 水晶宫与树


| 机制 / Skill                                                     | 做什么                      |
| -------------------------------------------------------------- | ------------------------ |
| **Crystal Vault（S）**                                           | 根级原文；S-Filter            |
| **Arbor Anchors（A）**                                           | 已确认结构/配方                 |
| `memory-systems` / `filesystem-context` / `writing-for-agents` | 记忆架构 · 落盘指针 · Agent 文档写法 |


### 4. Build — 实现与反馈


| Skill                                            | 做什么                      |
| ------------------------------------------------ | ------------------------ |
| `implement` / `implement-spec`                   | 按规格交付                    |
| `tdd` / `diagnosing-bugs` / `code-review` / `pr` | 红绿重构 · 诊断 · 双轴评审 · PR 形状 |
| `research` / `wizard`                            | 调研落盘 · 人机向导              |


### 5. Orchestrate & Context


| Skill                                                                                                | 做什么                                |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------- |
| `multi-agent-patterns` / `hosted-agents` / `latent-briefing` / `tool-design` / `harness-engineering` | 多 Agent · 沙箱 · 高效交接 · 工具 · harness |
| `context-fundamentals` / `degradation` / `compression` / `optimization` / `self-managed-context`     | 注意力 · 失忆诊断 · 压缩 · 优化 · 自管理上下文      |


### 6. Handoff · Evaluate · Tune · Shape


| Skill                                                                                  | 做什么                   |
| -------------------------------------------------------------------------------------- | --------------------- |
| `handoff` + 保真分区模板                                                                     | 下一棒可接力                |
| `evaluation` / `advanced-evaluation`                                                   | 评测 · LLM-as-Judge     |
| **control-variable-tune**                                                              | 卡住时的科学调参              |
| `retro` / `self-improvement-loops` / `instruction-surface-security`                    | 复盘 · 自改进 · 指令面安全      |
| `improve-codebase-architecture` / `codebase-design` / `triage` / `project-development` | 防泥球 · 深模块 · 分拣 · 项目成型 |


————————————————————————

## 仓库里有什么


| 路径 | 说明 |
|------|------|
| `crystal-palace/palace_cli.py` | **可运行 runtime**：Vault / S-Filter / Brief / Handoff / Tune |
| `crystal-palace/vault/` | Crystal Vault（S/A/leaves/pending/audit） |
| `crystal-palace/state/` | brief · handoff · filter 报告 · tune/reject 日志 |
| `.cursor/skills/` | palace-orchestrator · crystal-palace-memory · lean-handoff · control-variable-tune |
| `.cursor/rules/crystal-palace.mdc` | S 级硬约束（alwaysApply） |
| `skills-source/` | 对齐 / 上下文 / 工程交付技能源与审计文档 |

### 快速开始（成熟 skill 安装）

```bash
# 一键装到 Cursor + Claude Code + Codex，并生成 Grok 粘贴包
python crystal-palace/palace_cli.py install --target all
python crystal-palace/palace_cli.py doctor

# 运行时自检
python crystal-palace/palace_cli.py self-test
python crystal-palace/palace_cli.py demo
```

| 平台 | 安装产物 |
|------|----------|
| Cursor | `.cursor/skills/*` + `.cursor/rules/crystal-palace.mdc` |
| Claude Code | `.claude/skills/*` + `CLAUDE.md` + `.claude/rules/` |
| Codex | `.agents/skills/*` + `AGENTS.md` |
| Grok | 仓库根 `GROK.md`（粘贴自定义指令；Cursor 里选 Grok 则直接用 Cursor skills） |

```bash
# 单平台 / 用户全局 / 卸载
python crystal-palace/palace_cli.py install --target claude
python crystal-palace/palace_cli.py install --target codex --scope user
python crystal-palace/palace_cli.py install --target all --uninstall
```

工作流：

1. 模糊需求 → **grill-me** / `grilling`
2. `brief-init --predicate "..."` → 填 `state/brief.md`
3. 硬要求 `s-add`；派工前 `s-filter --task "..."`（BLOCK 则停）
4. 沿 A 级结构实现（tdd / review）
5. `handoff --task "..."` 保真交接
6. 连否 `reject`×3 → `tune-start` → `tune-score` → `tune-decide`

安装说明：[`crystal-palace/INSTALL.md`](crystal-palace/INSTALL.md) · 包结构：[`crystal-palace/PACKAGE.md`](crystal-palace/PACKAGE.md)

————————————————————————

## End-to-end

```text
模糊需求
   → Align (grilling)
   → Explicit Brief (E)
   → Crystal Vault + S-Filter (P)
   → Grow from Arbor (A)
   → Build with feedback
   → Lean Handoff (L)
   → 卡死则 Control-variable (C) → 固化或回滚
```

————————————————————————

## Roadmap

- [x] 对齐 · 上下文 · 工程交付 skills 入库  
- [x] 总调度桥接 `clarify-then-brief` / `palace-orchestrator`  
- [x] Crystal Vault / Arbor 落盘与 S-Filter 可执行化（`palace_cli.py`）  
- [x] 保真交接模板固化（`handoff` + auto S-Filter）  
- [x] `control-variable-tune`（CLI + skill；`promote-a` 可写入 Arbor）  
- [x] 仓库级规则：`.cursor/rules/crystal-palace.mdc`  
- [x] 多 Agent 适配安装器：`install --target cursor|claude|codex|grok|all`  
- [ ] 可选：S-Filter 语义检索 / 多 vault 工作区  
- [ ] 可选：与 issue tracker 工单字段双向同步

————————————————————————

**Crystal Palace：不是更多废话 Prompt，而是更少遗忘、更可对齐、更可收敛的协作。**

*The final form of human–agent collaboration.*