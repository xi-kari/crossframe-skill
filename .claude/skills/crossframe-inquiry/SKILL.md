---
name: crossframe-inquiry
description: 经由 crossframe-suite 调度使用，不独立响应。把 CrossFrame 诊断、文章、review、claim ledger 和机制候选转化为结构追问，帮助用户继续深思、反证、补证、迁移应用或收束。
trigger: suite-only
disable-model-invocation: true
---

# CrossFrame Inquiry / 结构追问层

## 定位

本 skill 负责把已经完成的 CrossFrame 分析转化为可继续思考的追问路径。

它不是新的诊断层，不重新生成正文，不替代 `crossframe-review`，也不把用户带向预设结论。它只从已完成的 `claim ledger`、`mechanism_candidates`、证据缺口、`concept_contracts` 和 review 结果中，选择最值得继续思考的 3-5 个主追问点，并可附加最多 2 个可选深挖问题。

## 启动条件

只在 suite 调度下启动：

- 上一轮 `crossframe-suite` 已完成 `crossframe -> ... -> crossframe-essay -> crossframe-review`，并写入 `post_completion_inquiry_armed=true`；此后完成态后续输入默认进入本 skill。
- 用户在 CrossFrame 输出后问“继续追问我”“我该继续想什么”“帮我继续思考”“更深一点”“下一步怎么分析”。
- 用户反对结论、要求反证、补证、迁移到另一个案例、行动边界或自我定位。
- review 后仍有未闭合 claim、证据缺口、概念契约 partial/fail、正文强度风险或可迁移问题。
- 教学、读书、历史、组织、公共、关系、案例等任务需要继续展开思考，而不是再写一篇文章。

不得在用户只要求最终答案、短答、翻译、格式化、纯改写时启动。

## 完成态后续输入接管

当 `crossframe-suite` 完整链路已经完成，且上一轮状态包含 `post_completion_inquiry_armed=true` 时，后续用户输入不再按普通新任务理解，而是先按“对上一轮输出的继续追问”处理。用户无论是说“嗯”“展开一下”“那我呢”“这能行动吗”“不太同意”“换个角度”“继续”“所以呢”，都默认进入本 skill。

本 skill 必须主动回收上一轮 `claim ledger`、机制候选、概念契约、结构洞察底稿、文章正文和 review 结果，建立上游上下文索引，再判断当前输入属于反证、补证、迁移、行动边界、自我定位、概念保真或收束。不得重新启动默认 essay，不得把后续输入当作孤立短答。

只有用户明确说“新任务 / 换主题 / 退出追问 / 不接着上文 / 不要用刚才那套分析”时，才解除 `post_completion_inquiry_armed`，回到 suite 普通路由。

## 输入依赖

优先复用上游材料，不重新发明判断：

- `post_completion_inquiry_armed` 状态
- `v5-read-state-capsule`
- `claim ledger`
- `mechanism_candidates`
- `source ledger`
- `concept_contracts`
- `crossframe-review` 结果
- 文章正文或结构洞察底稿
- 用户刚表达的困惑、反对、兴趣点或选择

必要时，本 skill 可以启动 `sibling_knowledge_retrieval`：把其它 CrossFrame sibling skill 的协议、references 和 templates 当作知识库检索来源，用于补充追问对象、边界条件和问题类型。

若上游缺少 `claim ledger`，本 skill 不补完整诊断，只能生成轻量追问，并提醒需要先回到 `crossframe` 补台账。

## Sibling 知识库检索

`crossframe-inquiry` 允许定向读取 sibling skill，但只用于“找该问什么”和“补足追问边界”，不用于替 sibling skill 下新结论。

可检索来源包括：

- `crossframe`：概念卡、诊断协议、七闸、claim ledger、源锚点与连续联读包。
- `crossframe-org`：组织迁移、责任链、授权链、反馈写回、低风险试点边界。
- `crossframe-public`：公共事实、平台治理、证据阶梯、机构合规、风险语言边界。
- `crossframe-history`：历史史料档位、史料台账、历史因果降级、历史接口边界。
- `crossframe-notebook`：外部文本吸收、关联/不同、可吸收处与冲突处。
- `crossframe-debate`：命题反证、最强反方、隐藏前提。
- `crossframe-dialogue`：读者回应、自我定位、短答复中的承接边界。
- `crossframe-teach`：概念解释、误读纠偏、微练习。
- `crossframe-casebook`：案例复用、脱敏事实边界、机制沉淀。
- `crossframe-critical`：批判矩阵、例子与点睛句的 claim_id 绑定边界。

检索规则：

1. 先用上一轮上下文和用户本轮输入确定检索目标。
2. 只读取 1-3 个相关 sibling skill，不得为了完整而读取全部 sibling skill。
3. 只读必要协议、references、templates；默认不读 examples 和 evals，除非要查失败模式。
4. 按 `templates/knowledge-retrieval-log.md` 写 `retrieval_log`：记录 `skill_id`、文件路径、检索目的、可用于哪些问题、不能证明什么。
5. 检索材料只能生成或收紧追问，不得把检索材料直接写成新结论。
6. 如果检索后发现需要公共事实判断、组织修复方案、历史史料判断或正式评审，必须回到 suite 路由对应 sibling skill。

## 必须执行的顺序

1. 读取上游输出，不新增中心判断。
2. 若处于 `post_completion_inquiry_armed=true`，先建立上一轮上下文索引：`claim ledger`、`mechanism_candidates`、`source ledger`、`concept_contracts`、结构洞察底稿、文章正文、review warnings、用户本轮输入。
3. 判断是否需要 `sibling_knowledge_retrieval`；若需要，定向读取相关 sibling skill 内容并生成 `retrieval_log`。
4. 找出可追问对象：`unresolved_claims`、`weak_evidence_claims`、`mechanism_candidates`、`concept_contract partial / fail`、用户张力、行动边界、尺度边界和 review warnings。
5. 按 `templates/inquiry-state.md` 生成 `inquiry_state`。
6. 根据任务选择 1-2 个追问模式：理解型、反证型、补证型、迁移型、自我定位型、行动边界型、概念保真型。
7. 每轮只给 3-5 个主问题，最多 2 个可选深挖问题。
8. 每个问题必须绑定 `q_id`、来源 `claim_id` 或 `mechanism_id`、`question_type`、`purpose`、`expected_answer_type` 和 `risk_boundary`。
9. 用户回答后先生成 `templates/user-answer-digest.md`，再决定回到原 claim、生成 followup question、标记证据缺口、降档，或进入 essay/review/dialogue。
10. 不得把用户回答直接写成新结论。若用户回答产生新事实、新证据或新判断，必须生成 `inquiry_claim_delta` / `claim ledger delta`，再回交 `claim ledger`。

## 输出规则

默认输出不超过 5 个问题。问题必须具体、可回答、不诱导、有对象、有边界，并能改变后续路径。

不得只写：

```text
你怎么看？
你觉得呢？
还有什么？
这说明了什么？
```

应写成：

```text
针对 CL2，你现在更想验证它的事实依据，还是想挑战它的解释路径？
如果要反驳 M1，最强反例应该来自哪类材料？
这个判断对你现实问题的意义，是解释过去、判断当下，还是决定下一步行动？
```

## 硬规则

- 不得制造新中心命题。
- 不得诱导用户接受 CrossFrame 的原判断。
- 不得新增未登记判断。
- 不得把追问变成心理审判、人格判断、概念考试或行动催促。
- 不得让用户承担不该承担的责任。
- 高责任、亲密关系、公共指控、组织处置、法律/医疗/财务等场景，追问必须优先保护边界和行动上限。
- 若用户回答中出现新事实、新证据、新判断，必须标记为 `inquiry_delta` / `inquiry_claim_delta`，不得直接并入原结论。
- 若追问产生新的强判断需求，必须回到 `crossframe` 或 `crossframe-review`，不得在 inquiry 内直接升级。

## 最低合格标准

- 是否明确追问对象来自哪个 `claim_id`、`mechanism_id` 或 review warning？
- 是否说明这个问题为什么值得问？
- 是否避免把用户带向预设答案？
- 是否能让用户继续思考事实、机制、前提、反例、证据或行动边界？
- 是否保留退出条件：用户可以选择“不继续追问，收束为摘要”？
