---
name: crossframe-essay
description: CrossFrame Essay 是基于 CrossFrame 的中文批判性洞察文章写作 skill。Use when the user asks to write 中文文章、长文、评论、思想文章、批判性洞察文章、结构洞察文章，或把关系、团队、组织、制度、公共议题、哲学概念和复杂现实问题写成面向普通读者、可按需概念上升并引入中西经典/理论参照的文章。也适合亲切、编辑、同志口吻、报刊答复、耐心解答或给意见的中文文章。默认先输出结构洞察底稿，再输出文章正文；也支持互动打磨和逐段推进。
---

# CrossFrame Essay for Claude Code

本 Claude Code skill 是薄适配层。权威主体在 `skills/crossframe-essay/SKILL.md`，推理引擎来自 `skills/crossframe/`。

使用时必须：

1. 读取 `skills/crossframe-essay/SKILL.md`。
2. 读取 `skills/crossframe/SKILL.md`。
3. 读取 `skills/crossframe/references/read-routing-map.md`，把主题路由到对应 CrossFrame protocol。
4. 读取 `skills/crossframe-essay/references/evidence-and-search-rules.md`，决定是否查源。
5. 需要思想深度、概念上升、引经据典或理论参照时，读取 `skills/crossframe-essay/protocols/concept-elevation-protocol.md`、`skills/crossframe-essay/references/reference-and-allusion-rules.md` 和 `skills/crossframe-essay/references/concept-reference-map.md`。
6. 自动成文默认读取 `skills/crossframe-essay/protocols/editorial-comrade-voice-protocol.md` 与 `skills/crossframe-essay/references/editorial-voice-principles.md`；只有显式中性报告、备忘录、表格、纯诊断或学术摘要时关闭。
7. 自动成文读取 `skills/crossframe-essay/protocols/essay-protocol.md` 与对应模板，默认执行 `full-visible-v3-longform`。
8. 互动打磨读取 `skills/crossframe-essay/protocols/interactive-drafting-protocol.md` 与互动模板。
9. 默认输出完整可见 `结构洞察底稿`，再输出完整长文 `文章正文`。

硬规则：

- 不要只写正文，不给底稿。
- 不要只写底稿，不给完整长文正文；不要把自动成文压缩成短答。
- 不要用检索材料接管文章命题。
- 不要用经典/理论参照接管文章命题；参照必须回到现实机制、证据和责任链。
- 直接引用必须可核验；不确定原句时只做意译或思想映射。
- 现代编辑底色只负责表达：亲切但不和稀泥，果敢但不人格审判，不复古口号化。
- 不要把批判写成人格审判。
- 前台用普通中文，后台保留 CrossFrame 概念链。
- 公共议题、最新事实、真实组织/平台/人物/政策/公司相关内容必须查源并标注证据边界。
- 私人关系、哲学概念和泛论随笔默认不查源，除非用户要求。
