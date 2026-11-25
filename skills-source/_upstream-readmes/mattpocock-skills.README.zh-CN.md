# 给真工程师用的 Skills（中文译文）

> 原文：[mattpocock/skills README](./mattpocock-skills.README.md)

这些是我每天用来做**真工程**的 Agent Skills——不是 vibe coding（凭感觉瞎聊出代码）。

做真实应用很难。GSD、BMAD、Spec-Kit 这类方法想帮你，靠的是**接管整套流程**。但这样一来，控制权被拿走了，流程里出了 bug 也很难修。

这些 skill 的设计目标是：**小、好改、可组合**。任何模型都能用。背后是几十年工程经验。随便改、据为己有、玩得开心就好。

想跟更新、看新 skill，可以订阅通讯（约 6 万人）：  
[Sign Up To The Newsletter](https://www.aihero.dev/s/skills-newsletter)

---

## 安装（大约 30 秒）

- **插件**：会自己更新。  
- **[skills.sh](https://skills.sh/mattpocock/skills)**：把可编辑文件拷进项目，更新要自己手动。  

每个 Agent **二选一**装一种；两种都装会导致每个 skill 出现两份。

### 1. 拿到 skills

（各平台安装命令见原文；Cursor 可用：）

```bash
npx skills@latest add mattpocock/skills -a cursor
```

安装器问选哪些时，记得带上 `setup-matt-pocock-skills`。更新用 `npx skills@latest update`，新 skill 再跑一次 `add`。

### 2. 跑一次 `/setup-matt-pocock-skills`

每个仓库跑一次。它会问你：

- 用哪种 issue 追踪（GitHub / GitLab / 本地文件 / 你描述的其他）
- triage 时用什么标签（`/triage` 会用到）
- 文档要存到哪里

### 3. 完事，可以开工。

---

## 为什么要有这些 Skills

我写它们，是为了修 Claude Code、Codex 等 coding agent 上常见的**失败模式**。

### #1：Agent 做的不是我想要的

> 「没人一开始就精确知道自己想要什么。」——《程序员修炼之道》

**问题**：软件开发最常见的失败是**对齐失败**。你以为对方懂了；看到成品才发现完全不是一回事。

AI 时代一样：人和 Agent 之间有沟通鸿沟。解法是一场 **grilling session（拷问式访谈）**——让 Agent 就「你要建什么」把你问细。

**解法**：

- `/grill-me` —— 非代码场景也能用  
- `/grill-with-docs` —— 同 `/grill-me`，但多一些文档能力（见下）

这是我最火的 skill。动手前先对齐，把这次改动想透。**每次要改东西都该用。**

### #2：Agent 话太多

> 有了通用语言（ubiquitous language），开发者聊天和代码表达都来自同一套领域模型。——《领域驱动设计》

**问题**：项目初期，开发和领域专家常常说两套话。Agent 也一样：扔进项目里边做边猜黑话，于是能用 1 个词说清的事，它用 20 个词。

**解法**：**共享语言**——一份帮 Agent 解码项目黑话的文档。

例子（同一意思）：

- **之前**：「课程某一章里的一课被『做实』（即在文件系统里有了位置）时会出问题」  
- **之后**：「物化级联（materialization cascade）有问题」

这种简洁，会在一次次会话里持续回报。

这写进了 `/grill-with-docs`：一边拷问，一边和 AI 共建共享语言，并把难讲清的决策记进 ADR。

很难说清这有多强——可能是本仓库**最酷的一招**。自己试一次就懂。

> 共享语言不止少废话：  
> - 变量/函数/文件命名一致  
> - 代码库更好导航  
> - Agent 思考更省 token（语言更紧）

### #3：代码根本不能跑

> 「永远小步、有意为之。反馈速率就是你的速度上限。别接太大的任务。」——《程序员修炼之道》

**问题**：就算对齐了要做什么，Agent **还是**可能产出垃圾。该看**反馈环**了。看不到代码实际跑得怎样，Agent 就是盲飞。

**解法**：常见反馈环——静态类型、浏览器、自动化测试。

测试里关键是 **红-绿-重构**：先写失败测试，再写代码让它绿。反馈稳定了，代码质量会好很多。

- `/tdd` —— 可插进任何项目的 TDD skill  
- `/diagnosing-bugs` —— 把调试最佳实践收成有纪律的循环，分阶段放行

### #4：我们堆出了一坨泥球

> 「每天都要投资系统的设计。」——Kent Beck  
> 「最好的模块是深的：简单接口背后大量行为。」——John Ousterhout

**问题**：多数用 Agent 做出的应用复杂、难改。Agent 加速写代码的同时，也加速**软件熵增**——复杂度以前所未有的速度涨。

**解法**：对 AI 开发来说有点「激进」的一招——**认真关心代码设计**。

写进各层 skill，例如：

- `/to-spec` 写规格前会问你要动哪些模块  
- `/improve-codebase-architecture` 扫描代码库找「加深模块」的机会，给你候选。建议隔几天跑一次。它是**勘察**，不是**救灾**：老仓库能找到真机会，但不会替你把泥球解开。

### 小结

软件工程基本功比以往更重要。这些 skill 是我尽力把基本功压成**可重复做法**，帮你交出职业生涯最好的应用。玩得开心。

---

## 技能目录说明

按「谁能调用」分两类：

- **用户调用（User-invoked）**：只有你键入才触发（如 `/grill-me`），负责编排。  
- **模型调用（Model-invoked）**：你能调，Agent 觉得合适也会自动调；装的是可复用纪律。  

规则：用户调用的可以调用模型调用的；**用户调用的不要互相调用**。

### Engineering（工程，日常写代码用）

**用户调用**

| Skill | 干什么 |
|-------|--------|
| ask-matt | 问该用哪个 skill/流程；本仓库用户技能的路由器 |
| grill-with-docs | 拷问 + 建领域模型，打磨术语，更新 `GLOSSARY.md` 和 ADR |
| triage | 用状态机推进 issue 的分拣角色 |
| improve-codebase-architecture | 扫描「加深」机会，HTML 报告，再对你选中的那条做 grilling |
| setup-matt-pocock-skills | 每个仓库先跑一次：配置 tracker、标签、文档布局 |
| to-spec | 把当前对话收成规格发到 tracker；不再访谈，只综合已讨论内容 |
| to-tickets | 计划/规格/对话拆成 tracer-bullet 工单，写清阻塞关系 |
| implement | 按规格/工单实现；在预定接缝跑 `/tdd`，提交前 `/code-review` |
| implement-spec | 整份规格在一条集成分支上实现；工单当任务图，子 Agent 并行扫就绪前沿 |
| wayfinder | 规划大到单会话装不下的活：在 tracker 上画决策地图，一次解一个 |
| retro | 会后建议改进 Agent 环境（导航、检查、规范、steering、工具），严重优先 |

**模型调用**

| Skill | 干什么 |
|-------|--------|
| prototype | 一次性原型回答设计问题（单 HTML 或多种 UI 可切换） |
| diagnosing-bugs | 难 bug/性能：造会红的反馈环 → 最小化 → 假设 → 埋点 → 修 → 回归 |
| research | 对高可信一手来源调研，结果写成带引用的 Markdown |
| tdd | 红绿重构；按垂直切片做功能/修 bug |
| domain-modeling | 主动打磨领域模型：对照词表、边界场景压测、更新 glossary/ADR |
| codebase-design | 「深模块」的共同纪律与词汇：小接口后大行为、干净接缝、可测 |
| code-review | 双轴评审：**规范** + **是否符合规格**；并行子 Agent，互不污染 |
| pr | PR 正文该长什么样：最小能说清改动的摘要、前后证据、合并风险 |
| wizard | 生成交互式 bash 向导，带人走只有人能做的步骤（配设施、密钥、第三方控制台等） |

### Productivity（生产力，不限写代码）

**用户调用**

| Skill | 干什么 |
|-------|--------|
| **grill-me** | 被无情拷问计划/设计，直到设计树每一枝都解决 |
| handoff | 把当前对话压成交接文档，给下一个 Agent 接着干 |
| teach | 跨多会话教你一门技能/概念，当前目录当有状态的教学空间 |
| to-questionnaire | 你答不了的决策 → 给能答的人的 Markdown 问卷；拷问的是「发给谁、要什么回」，不是题目本身 |
| wait-what | 话没听懂立刻用；Agent 用你缺的上下文、白话、按 `GLOSSARY.md` 重讲 |

**模型调用**

| Skill | 干什么 |
|-------|--------|
| **grilling** | 拷问原语；`grill-me`、`grill-with-docs`、`triage`、`wayfinder`、`improve-codebase-architecture` 背后都靠它 |
| writing-for-agents | 写给 Agent 读的文档：skill、AGENTS.md/CLAUDE.md、靠指针加载的文档 |

---

## 超短版（只记这个也行）

1. **对齐失败** → `/grill-me` 先问清楚再动手  
2. **话太多** → 建共享语言 / glossary  
3. **代码不行** → 反馈环：`/tdd`、`/diagnosing-bugs`  
4. **越写越乱** → 天天关心设计：`/improve-codebase-architecture`  

Skill 要**小、可组合、你能改**；别把整套流程控制权交给一个黑盒大框架。
