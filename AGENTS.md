# CrossFrame / Agent Adapter

本文件是给通用 AI agent 的仓库级入口说明。仓库主体仍以 [README.md](README.md)、[skills/crossframe-suite/SKILL.md](skills/crossframe-suite/SKILL.md)、[skills/crossframe/SKILL.md](skills/crossframe/SKILL.md) 与 [skills/crossframe-essay/SKILL.md](skills/crossframe-essay/SKILL.md) 为准。

## 仓库怎么理解

- `skills/crossframe-suite/`：CrossFrame skill family 总调度入口，负责连续触发顺序和质量闸。
- `skills/crossframe/`：真正可安装的 Codex skill 主体。
- `skills/crossframe-essay/`：平行文章写作 skill，把 CrossFrame 结构判断转成中文批判性洞察文章。
- `skills/crossframe-review/`：评审 CrossFrame 输出是否真推理、守证据和边界。
- `skills/crossframe-dialogue/`：答读者问、编辑回信和咨询式短答复。
- `skills/crossframe-casebook/`：把材料整理成可复用案例库。
- `skills/crossframe-public/`：公共议题、平台申诉、制度评论和合规材料专项。
- `skills/crossframe-org/`：团队、项目、组织修复专项。
- `skills/crossframe-teach/`：CrossFrame 概念教学解释专项。
- `skills/crossframe-debate/`：命题辩论与论证检验专项。
- `skills/crossframe-notebook/`：读书、理论和文章研究笔记专项。
- `skills/crossframe/protocols/`：诊断、推演、开放断言、反俘获、低条件行动协议。
- `skills/crossframe/worksheets/`：intake、五闸、证据账本、机制候选等推理发动机。
- `skills/crossframe/references/read-routing-map.md`：按请求类型决定要读哪些协议、工作表、概念卡和模板。
- `skills/crossframe/references/v3-term-fidelity.md`：v3.0 术语保真层，防止压缩后概念失真。
- `skills/crossframe/references/v3-source-spine.md`：v3.0 DOCX 源结构脊柱，记录章节顺序、相邻关系和承接状态。
- `skills/crossframe/references/v3-section-digest-index.md`：逐节保真摘要索引，防止读少或断章。
- `skills/crossframe/references/continuity-bundles.md`：连续联读包，规定哪些概念不能只读单卡。
- `skills/crossframe/references/theory-backend-index.md`：长期演化、根假设、阶段、递进、多中心治理等深水区索引。
- `skills/crossframe/references/v3-coverage-map.md`：v3.0 重要模块到 skill 文件的覆盖地图，维护时用于查漏。
- `skills/crossframe/templates/`：用户可见输出模板，默认包含推理提纲。
- 适配层：`CLAUDE.md`、`.claude/skills/crossframe*/SKILL.md`、`.claude/commands/crossframe*.md`、`GEMINI.md`、`.cursor/rules/crossframe*.mdc`、`.github/copilot-instructions.md`、`.windsurf/rules/crossframe.md`、`.clinerules/crossframe.md`、`.roo/rules/crossframe.md`、`.continue/rules/crossframe.md`、`CONVENTIONS.md`、`.aider.conf.yml`、`llms.txt`。

## 何时调用 CrossFrame

默认优先判断是否使用 `skills/crossframe-suite/SKILL.md`。当用户要文章、公共评论、组织复盘文章、读书后成文、辩论后成文、案例沉淀再输出、或要求多个 CrossFrame skill 连续协作时，先读 suite，再按它的 `workflow-routing-map.md` 进入专项 skill。

如果用户没有指定交付物，只是说“分析一下”“怎么看”“讲讲这个问题”“写一下这个主题”或“给我一个有洞察的回答”，suite 默认最终输出可读文章或文章式回答：`crossframe -> crossframe-essay -> crossframe-review`。如果用户明确要评审、案例库、组织备忘录、反馈写回方案、命题辩论表、概念教学练习、来源台账、表格、清单、一句话结论、低条件行动方案或纯诊断，不要擅自生成文章。

当任务涉及以下内容时使用：

- 关系、团队、项目、组织、制度、公共争议中的复杂失衡
- 需要结构诊断、推演、路径展开、后续走向或分支终点
- 需要开放断言，而不是强行给终局判断
- 证据不足但风险紧急，需要低条件试探行动
- 高权力密度、高责任场景，需要反俘获审查
- 强判断、高反身性对象、亲密关系、疗愈转移、公共制度、框架边界、生命周期、递进、势场/自主解离、治理连续性、超大规模压力测试或长期演化问题
- 哲学、意义、生命第一因、虚无主义等抽象问题，需要先做概念解释、尺度拆分和结构性开放断言
- 用户希望分析复杂反复问题，但不要概念堆砌

不要用于：

- 单纯事实查询
- 代码实现、算术、工具操作等非结构诊断任务
- 医疗、法律、金融等需要专业资质的最终判断
- 用户只是需要安慰，不需要诊断分析的对话

## 何时调用 CrossFrame Essay

若写作任务还涉及公共事实、组织修复、命题辩论、读书研究、案例沉淀或最后评审，先使用 `skills/crossframe-suite/SKILL.md` 决定链路；不要直接只触发 essay。

当任务涉及以下内容时使用 `skills/crossframe-essay/SKILL.md`：

- 用户要求写中文文章、长文、评论、思想文章、批判性洞察文章或结构洞察文章
- 用户想把 CrossFrame 分析结果转成普通读者能读的文章
- 用户希望文章上升概念、引经据典、加入理论参照、历史经验或文学互文
- 用户希望文章像一位现代编辑同志耐心、谦逊、认真、果敢地回应读者问题
- 用户给出零散素材，希望整理成有中心命题、有递进、有边界的长文
- 主题是关系、团队、组织、制度、公共议题或哲学概念，但目标是“成文”而不是只要诊断

CrossFrame Essay 仍然必须读取 `skills/crossframe/SKILL.md` 与 `skills/crossframe/references/read-routing-map.md`。默认输出顺序是 `结构洞察底稿` -> `文章正文`。

如果启用概念上升，先从结构机制抽象上位概念，再选择中西经典、历史经验、理论或文学互文，最后回落到现实责任链。直接引用必须可核验；不确定原句时只做意译或思想映射。

自动成文默认启用现代编辑底色，先在底稿中写出 `正文声口方案`，再成文。问题型主题用答复体，公共评论、思想文章和概念文章用评论体。只有用户明确要求中性报告、备忘录、表格、清单、纯诊断或学术摘要时才关闭；不要复古口号化，不要把亲切写成和稀泥，也不要把严厉写成人格审判。

## 何时调用其它平行 skill

- 审查、评审、打分、抓坏输出、判断是否真的推理：`skills/crossframe-review/SKILL.md`
- 答读者问、编辑回信、咨询式短答复、我该怎么看/怎么办：`skills/crossframe-dialogue/SKILL.md`
- 整理聊天记录、组织材料、项目复盘、公共争议为案例库：`skills/crossframe-casebook/SKILL.md`
- 公共议题、平台申诉、制度评论、机构合规材料、公共承诺兑现：`skills/crossframe-public/SKILL.md`
- 团队、项目、组织修复、复盘改造、反馈写回、低风险试点：`skills/crossframe-org/SKILL.md`
- CrossFrame 概念教学、误读纠偏、现实信号、练习题：`skills/crossframe-teach/SKILL.md`
- 命题、争论、正反双方、隐藏前提、证据要求、撤回条件：`skills/crossframe-debate/SKILL.md`
- 读书、理论、文章、摘录研究笔记，比较关联与不同：`skills/crossframe-notebook/SKILL.md`

这些平行 skill 都必须保持轻入口：先读取各自 `SKILL.md`，再按其说明读取 `skills/crossframe/SKILL.md` 和 `skills/crossframe/references/read-routing-map.md`；不得复制 CrossFrame 全文。

## 连续触发规则

默认链路：

- 结构诊断：`crossframe`
- 普通洞察文章：`crossframe -> crossframe-essay -> crossframe-review`
- 公共评论文章：`crossframe -> crossframe-public -> crossframe-essay -> crossframe-review`
- 组织复盘/修复文章：`crossframe -> crossframe-org -> crossframe-essay -> crossframe-review`
- 答读者问：`crossframe -> crossframe-dialogue -> review-lite`
- 案例沉淀：`crossframe -> crossframe-casebook -> crossframe-review`
- 概念教学：`crossframe -> crossframe-teach -> review-lite`
- 命题辩论：`crossframe -> crossframe-debate -> crossframe-review`
- 辩论后成文：`crossframe -> crossframe-debate -> crossframe-essay -> crossframe-review`
- 读书研究：`crossframe -> crossframe-notebook -> crossframe-review`
- 读书后成文：`crossframe -> crossframe-notebook -> crossframe-essay -> crossframe-review`

连续触发时先给短 `调度提纲`：任务类型、工作流、必读 skill、按需读取、不读取、质量闸。不要为了完整而读取全部 skill。

开放式分析默认成文；明确指定非文章交付物时保留原形态。

## 必须遵守

1. 中文为权威语义，英文只作传播名或文件名。
2. 先形成内部推理产物，再输出结论。
3. 默认先展示简短推理提纲：
   - 诊断对象
   - 事实边界
   - 尺度窗口
   - 机制候选
   - 判断档位
   - 本次读取的概念
   - 下一步
4. 先说人话，再按需补术语映射。
5. 至少列两个机制候选，除非证据足以排除其他可能。
6. 不把结构诊断变成人格审判、宿命判断或责任稀释。
7. 开放断言必须包含证据、替代解释、撤回条件和行动边界。
8. 如果使用承接/回流、开放断言、尺度转移、观测反身性、权力封闭、低条件试探行动、爱/开放行动、主体/责任链、证据成本、机制候选、判断档位、退出转移、修复副产品等高风险概念，先读取 `skills/crossframe/references/concept-cards/README.md` 与对应概念卡。
9. 输出前用 `skills/crossframe/worksheets/concept-fidelity-check.md` 检查概念是否读全、是否落到现实行为、是否避免压缩失真。
9.1 输出前按需用 `skills/crossframe/worksheets/source-continuity-check.md` 检查是否触发 3.0 连续联读包；高责任、公共制度、亲密关系、长期演化、深度分析和文章输出不能只读单张概念卡。
10. 强判断必须走命题验证；高反身性对象必须有限收束；亲密关系先保护痛苦、安全和边界；疗愈转移不替代专业干预。
11. 框架边界问题不得把 CrossFrame 当专业替代品；生命周期不得写成命运；超大规模判断必须写不可判断区。
12. 哲学/意义类问题不要机械退回“不可诊断”；先尝试结构化解释，只有无法结构化时才退回框架边界。

## 读取优先级

0. 复杂多交付任务先读 [skills/crossframe-suite/SKILL.md](skills/crossframe-suite/SKILL.md) 与 `skills/crossframe-suite/references/workflow-routing-map.md`
1. [skills/crossframe/SKILL.md](skills/crossframe/SKILL.md)
2. 先读取 `skills/crossframe/references/read-routing-map.md` 确定本次路由
2.1 需要连续保真时读取 `skills/crossframe/references/continuity-bundles.md`、`skills/crossframe/references/v3-source-spine.md`、`skills/crossframe/references/v3-section-digest-index.md` 与 `skills/crossframe/worksheets/source-continuity-check.md`
3. 普通诊断读取 `skills/crossframe/protocols/diagnosis-protocol.md`
4. 推演读取 `skills/crossframe/protocols/inference-protocol.md`
5. 开放断言读取 `skills/crossframe/protocols/open-assertion-protocol.md`
6. 高责任场景读取 `skills/crossframe/protocols/anti-capture-protocol.md`
7. 证据不足但紧急读取 `skills/crossframe/protocols/low-condition-action-protocol.md`
8. 概念解释读取 `skills/crossframe/protocols/concept-explanation-protocol.md`
9. 强判断读取 `skills/crossframe/protocols/proposition-verification-protocol.md`
10. 高反身性读取 `skills/crossframe/protocols/high-reflexivity-protocol.md`
11. 亲密关系读取 `skills/crossframe/protocols/intimate-relationship-protocol.md`
12. 疗愈转移读取 `skills/crossframe/protocols/healing-transfer-protocol.md`
13. 公共制度读取 `skills/crossframe/protocols/public-institution-protocol.md`
14. 框架边界读取 `skills/crossframe/protocols/framework-boundary-protocol.md`
15. 生命周期读取 `skills/crossframe/protocols/lifecycle-diagnosis-protocol.md`
16. 递进闭环读取 `skills/crossframe/protocols/progression-protocol.md`
17. 势场与自主解离读取 `skills/crossframe/protocols/field-dissociation-protocol.md`
18. 治理连续性读取 `skills/crossframe/protocols/governance-continuity-protocol.md`
19. 超大规模压力测试读取 `skills/crossframe/protocols/large-scale-stress-test-protocol.md`
20. 对外表达翻译读取 `skills/crossframe/protocols/expression-translation-protocol.md`
21. 长期演化或理论深水区读取 `skills/crossframe/references/theory-backend-index.md`
22. 输出前读取 `skills/crossframe/templates/reasoning-outline-output.md` 与对应输出模板
23. 高风险概念读取 `skills/crossframe/references/concept-cards/` 下的对应卡片

文章写作额外读取：

1. `skills/crossframe-essay/SKILL.md`
2. `skills/crossframe-essay/protocols/essay-protocol.md` 或 `interactive-drafting-protocol.md`
3. `skills/crossframe-essay/references/evidence-and-search-rules.md`
4. `skills/crossframe-essay/references/critical-insight-principles.md`
5. 概念上升读取 `skills/crossframe-essay/protocols/concept-elevation-protocol.md`、`references/reference-and-allusion-rules.md`、`references/concept-reference-map.md`
6. 自动成文默认读取 `skills/crossframe-essay/protocols/editorial-comrade-voice-protocol.md` 与 `references/editorial-voice-principles.md`；显式中性报告/备忘录/表格/纯诊断时才关闭
7. `skills/crossframe-essay/templates/insight-dossier-template.md`
8. `skills/crossframe-essay/templates/essay-output-template.md` 或 `interactive-session-template.md`

平行专项 skill 读取：

1. 先读对应 `skills/crossframe-*/SKILL.md`
2. 再读 `skills/crossframe/SKILL.md` 与 `skills/crossframe/references/read-routing-map.md`
3. 按专项 `protocols/`、`references/`、`templates/` 输出
4. 需要成文时才按需读 `skills/crossframe-essay/SKILL.md`

## 修改仓库时

- 不要把 `skills/crossframe/` 的可安装入口改丢。
- 不要把薄适配层扩写成另一份完整正文。
- 适配层必须保持薄入口：说明触发条件、读取顺序、输出闸，不复制完整协议。
- 新增概念前先确认它是否能进入工作表、闸门或模板，否则不要升格。
- 防失真材料优先放在 `references/` 和概念卡中，不要把 v3.0 全文塞回 `SKILL.md`。
- 新增或补齐 v3.0 概念时，同步更新 `skills/crossframe/references/v3-coverage-map.md`。
- 新增文章写作规则时，优先更新 `skills/crossframe-essay/`，不要把文章协议复制到根适配层。
- 改完后运行 skill 验证，并确认本地安装目录需要同步时已同步。
