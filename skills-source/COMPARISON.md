# grill-me vs Context Engineering：共同点与合并评估

## 本地位置

| 来源 | 路径 |
|------|------|
| mattpocock（grill 相关） | `01-grill-me/`（grill-me / grilling / handoff / grill-with-docs / writing-for-agents） |
| Context Engineering（核心子集） | `02-context-engineering/`（long-horizon-prompting / context-fundamentals / context-degradation / multi-agent-patterns / context-compression） |
| 完整 mattpocock 仓库 | `mattpocock/skills-main/` |

---

## 一句话定位

| | grill-me 族 | Context Engineering |
|--|-------------|---------------------|
| 本质 | **人机对齐协议**（问清楚再动手） | **Agent 系统工程**（上下文怎么管、长跑怎么写 brief） |
| 粒度 | 极短、可执行、会话内流程 | 教材级多 skill 体系 |
| 主用户 | 正在跟 Agent 一起做设计的人 | 在设计/调 Agent 系统的人 |

---

## 共同点（可合并的语义层）

### 1. 「先澄清，再行动」

- **grilling**：design tree + frontier 轮询，frontier 空了才算共享理解，才允许动手。
- **long-horizon-prompting**：先写 success predicate；写不出来就「不要 launch，先做 scoping session」。

同一思想，不同媒介：一个对着人问，一个写成可审计的 brief。

### 2. 「完成标准必须可判定」

- **writing-for-agents**：每个 step 要有 completion criterion（清晰 + 充分）。
- **long-horizon**：return condition = 对产物的谓词，而不是「我觉得差不多了」。
- **grilling**：会话结束条件 = frontier 为空 + 用户确认 shared understanding。

### 3. 「排除近似答案 / 近失」

- **grilling**：不问猜的问题；事实自己查，决策留给人；不默认假设。
- **long-horizon**：non-counting outcomes（缩小范围、综述、依赖未证命题……一律不算）。

都在堵「看起来像做完了」的逃逸口。

### 4. 「Handoff / 压缩保真」

- **mattpocock `handoff`**：压缩当前会话 → 给下一个 Agent 的交接文档；引用已有 artifact，不重复。
- **context-compression**：结构化 handoff summary（Intent / Files / Decisions / Next）；优化 tokens-per-task。
- **multi-agent-patterns**：显式 handoff 协议与状态传递。

交接是两边最硬的重叠点。

### 5. 「渐进披露 / 上下文指针」

- **writing-for-agents**：context pointer、progressive disclosure、认知负载 vs 上下文负载。
- **context-fundamentals**：progressive disclosure、attention budget、只加载高信号 token。

同一套「少而准」原则。

### 6. 「事实 vs 决策 / 执行 vs 验证」分离

- **grilling**：事实 = Agent 查；决策 = 用户拍板。
- **long-horizon + multi-agent**：生成与对抗审计分离；contract check 阻塞下游。

---

## 差异（不宜硬揉成一个文件）

| 维度 | grill-me | CE |
|------|----------|-----|
| 交互对象 | 主要是人 | 主要是 Agent / 系统 |
| 触发时机 | 动手前的访谈 | 启动长跑 / 诊断失忆 / 多 Agent 拓扑 |
| 体量 | grilling ≈ 30 行 | 单 skill 常 300–1000+ 行 |
| 产物 | 共享理解（口头/会话） | 伪形式任务书、压缩策略、拓扑 |
| 失败模式 | 乱猜需求、过早编码 | lost-in-middle、中毒、交接失真 |

**结论：语义可串联，文件不宜整库合并。**  
硬合成一个巨型 `SKILL.md` 会违反两边自己的原则（progressive disclosure / lean prompt）。

---

## 合并建议（推荐）

采用 **流水线桥接 skill**，不替换原 skill：

```text
模糊需求
   │
   ▼
[grilling]  ──人机拷问──► 共享理解 / 决策树
   │
   ▼
[long-horizon-prompting] ──形式化──► 成功谓词 + 不算清单 + handoff contract
   │
   ▼
执行（普通 Agent / 多 Agent）
   │
   ▼ 上下文吃紧
[handoff] 或 [context-compression] ──交接──► 下一会话
```

已生成的桥接 skill：`03-clarify-then-brief/SKILL.md`

可选加强（暂未并入）：

- 需要 ADR/术语表时：`grill-with-docs`
- 需要多 Agent 拓扑时：再加载 `multi-agent-patterns`
- 需要诊断「忘中间」时：再加载 `context-degradation`

---

## 合并可行性打分

| 方案 | 可行性 | 说明 |
|------|--------|------|
| A. 整库揉成一个 skill | ❌ 低 | 体量与受众冲突，违反披露原则 |
| B. 只把 grilling 塞进 long-horizon 的「Brief-Writing Workflow 第 0 步」 | ⚠️ 中 | 合理，但 CE 上游更新难跟 |
| C. 薄桥接 skill 串联调用 | ✅ 高 | 保留原 skill，组合最稳 |
| D. 只合并 handoff ↔ context-compression 的交接模板 | ✅ 高 | 局部合并价值最大 |

**推荐：C + D（桥接主流程 + 统一交接模板）。**
