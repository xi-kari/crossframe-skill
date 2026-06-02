# Gemini CLI 适配入口

@AGENTS.md

本文件是 Gemini CLI 的仓库级上下文入口。

如果用户要求一个复杂任务需要多个 CrossFrame skill 连续协作，先读取：

1. `skills/crossframe-suite/SKILL.md`
2. `skills/crossframe-suite/references/workflow-routing-map.md`
3. `skills/crossframe-suite/protocols/suite-dispatch-protocol.md`

常见链路：普通文章 `crossframe -> crossframe-essay -> crossframe-review`；公共评论 `crossframe -> crossframe-public -> crossframe-essay -> crossframe-review`；组织复盘文章 `crossframe -> crossframe-org -> crossframe-essay -> crossframe-review`；答读者问 `crossframe -> crossframe-dialogue -> review-lite`；读书后成文 `crossframe -> crossframe-notebook -> crossframe-essay -> crossframe-review`。不要一次读取全部 skill。

如果用户要求写中文文章、长文、评论、思想文章、批判性洞察文章或结构洞察文章，请读取：

1. `skills/crossframe-essay/SKILL.md`
2. `skills/crossframe/SKILL.md`
3. `skills/crossframe/references/read-routing-map.md`
4. 对应 `skills/crossframe/protocols/` 文件
5. `skills/crossframe-essay/references/evidence-and-search-rules.md`
6. 若需要概念上升、引经据典、理论参照或文学互文，读取 `skills/crossframe-essay/protocols/concept-elevation-protocol.md`、`skills/crossframe-essay/references/reference-and-allusion-rules.md`、`skills/crossframe-essay/references/concept-reference-map.md`
7. 若用户要求亲切、编辑、同志口吻、报刊答复、耐心解答或给意见，读取 `skills/crossframe-essay/protocols/editorial-comrade-voice-protocol.md` 与 `skills/crossframe-essay/references/editorial-voice-principles.md`
8. `skills/crossframe-essay/protocols/essay-protocol.md` 或 `interactive-drafting-protocol.md`
9. `skills/crossframe-essay/templates/insight-dossier-template.md`
10. `skills/crossframe-essay/templates/essay-output-template.md` 或 `interactive-session-template.md`

文章输出默认先给 `结构洞察底稿`，再给 `文章正文`。公共议题、最新事实、真实组织/平台/人物/政策/公司相关内容必须查源；私人关系、哲学概念和泛论随笔默认不查源，除非用户要求。直接引用必须可核验；不确定原句时只做意译或思想映射；经典/理论参照必须回到现实机制与责任链。现代编辑同志口吻只用于前台表达：亲切但不和稀泥，果敢但不人格审判。

如果用户要求结构诊断、推演、开放断言、高责任审查或低条件行动，请读取：

1. `skills/crossframe/SKILL.md`
2. `skills/crossframe/references/read-routing-map.md`
3. 对应 `skills/crossframe/protocols/` 文件
4. `skills/crossframe/templates/reasoning-outline-output.md`
5. `skills/crossframe/templates/user-facing-language.md`
6. 若使用高风险概念，读取 `skills/crossframe/references/concept-cards/README.md` 与对应概念卡
7. 输出前用 `skills/crossframe/worksheets/concept-fidelity-check.md` 做保真检查

输出要求：

- 先给简短推理提纲。
- 先说人话，不堆术语。
- 明确区分事实、解释、机制候选和判断档位。
- 中文概念不强行英文化。
- 前台少术语，后台不能少读必要概念。
- 强判断、高反身性、亲密关系、疗愈转移、公共制度、框架边界、生命周期、递进、势场解离、治理连续性、超大规模压力测试和长期演化问题，按 `read-routing-map.md` 读取对应深水区模块。

如果用户要求以下专项任务，优先读取对应平行 skill，再按该 skill 的说明读取 `skills/crossframe/SKILL.md` 与路由图：

- 评审、审查、打分、抓坏输出：`skills/crossframe-review/SKILL.md`
- 答读者问、编辑回信、咨询式短答复：`skills/crossframe-dialogue/SKILL.md`
- 案例库、材料沉淀、复盘转案例：`skills/crossframe-casebook/SKILL.md`
- 公共议题、平台申诉、制度评论、合规材料：`skills/crossframe-public/SKILL.md`
- 组织修复、反馈写回、复盘改造、低风险试点：`skills/crossframe-org/SKILL.md`
- 概念教学、误读纠偏、练习题：`skills/crossframe-teach/SKILL.md`
- 命题辩论、正反结构、撤回条件：`skills/crossframe-debate/SKILL.md`
- 读书、理论、文章研究笔记，关联与不同：`skills/crossframe-notebook/SKILL.md`
