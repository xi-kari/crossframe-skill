---
name: crossframe-review
description: |
  CrossFrame Review 是 CrossFrame 的平行评审 skill，用于审查 AI 输出、结构诊断、中文文章、审计稿或修复稿是否真正执行 CrossFrame 推理。Use when the user asks to review, audit, validate, grade, critique, find failures, smoke-test, or repair CrossFrame-style output, especially to catch concept stacking, pseudo-reasoning, missing evidence boundaries, personality judgment, forged or unverifiable citations, source search taking over the thesis, skipped structure dossier, AI compliance theater, and high-responsibility claims without proposition verification.
---

# CrossFrame Review

如果评审对象来自多个 CrossFrame skill 的连续工作流，先读取 `../crossframe-suite/SKILL.md` 还原应有调度链，再判断是否有漏触发、误触发或跳过质量闸。

本 skill 只做评审与修复建议，不替代 `crossframe` 生成诊断，也不替代 `crossframe-essay` 写文章。中文为权威语义；英文只作 skill id、文件名和接口说明。

## 轻入口规则

每次触发后，先读取 canonical skill，而不是复制它们的正文：

1. 读取 `../crossframe/SKILL.md`。
2. 读取 `../crossframe/references/read-routing-map.md`。
3. 若评审对象是文章、长文、评论、思想文章、报刊答复或“现代编辑同志口吻”输出，按需读取 `../crossframe-essay/SKILL.md`。
4. 读取本目录的 `protocols/review-protocol.md` 和 `templates/review-report.md`。
5. 若涉及文章底稿、引用、检索材料或声口，追加读取 `protocols/article-review-protocol.md`。
6. 按需读取本目录 `references/` 中的评分表、失败类型表和证据边界清单。

不要把 CrossFrame 主 skill 或文章 skill 的完整内容复制到本 skill 输出中。评审时只引用必要规则名、触发点和证据位置。

## 评审目标

判断一个输出是否真的完成了 CrossFrame 的最低推理链：

- 明确诊断或写作对象。
- 区分事实、解释、证据缺口和判断档位。
- 经过对象闸、证据闸、尺度闸、责任闸、观测闸。
- 至少形成两个机制候选，或说明为什么只能有一个。
- 对承担判断作用的高风险概念做保真检查，而不是把术语当结论。
- 给出可撤回条件、下一步观察或低条件行动边界。
- 文章类输出必须先有结构洞察底稿，再写正文。

## 必抓失败

以下问题一旦出现，要在评审中明确定位；严重时直接判为不合格：

- 概念堆砌：只堆“承接、回流、尺度、反俘获”等词，没有落回事实和行为。
- 伪推理：先给结论，再用术语装饰；没有机制候选、反向条件或证据闸。
- 事实边界缺失：把传闻、AI 报告、自评、搜索摘要或解释当事实。
- 跳过底稿：文章类输出直接成文，没有结构洞察底稿或等价内部骨架。
- 人格审判：把结构诊断变成“这个人坏、懒、无能、病态”等定性。
- 伪造引用：编造原文、页码、出处、作者观点；不确定原句却写成直接引用。
- 查源接管命题：检索材料决定文章立场，CrossFrame 只变成资料拼贴外壳。
- 强判断越级：处分、名誉、权利、资源、公共记忆类判断没有命题验证和申诉/反证入口。
- 尺度洗白：用宏观叙事取消低尺度痛苦、责任链或具体失职。
- AI 合规剧场：把 AI 生成材料、漂亮报告或自评文本当作独立强证据。

## 输出协议

默认使用 `templates/review-report.md`。最终评审必须包含：

- 评审对象
- 事实边界
- 触发规则
- 评分/等级
- 关键问题
- 证据定位
- 修复建议
- 是否合格

若用户只要一句话结论，也要保留“是否合格 + 主要失败点 + 下一步修复”的最小结构。

## 合格判定

评分只是辅助，硬失败优先：

- A：90-100，合格。
- B：75-89，条件合格，小修后可用。
- C：60-74，不合格，需要大修。
- D：40-59，不合格，需要重做主要推理。
- F：0-39 或触发硬失败，高风险失败。

触发人格审判、伪造引用、跳过文章底稿、强判断越级、证据边界完全缺失时，即使文字流畅，也不能判为合格。

## 修复原则

评审输出优先给可执行修复，不默认重写全文。除非用户要求“直接改写”，否则只给：

- 应补的事实边界。
- 应读取或声明的路由。
- 应新增的机制候选。
- 应降档的判断。
- 应删除或改写的人格审判、伪引用和术语堆砌句。
- 文章应补的结构洞察底稿项目。
