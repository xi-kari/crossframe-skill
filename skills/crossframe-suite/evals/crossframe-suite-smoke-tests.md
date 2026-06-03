# CrossFrame Suite Smoke Tests

## 1. 普通洞察文章

Prompt：写一篇“解释劳动为什么会耗竭”的文章。

期望：

- 工作流包含 `crossframe -> crossframe-essay -> crossframe-review`。
- 如果识别为关系困惑，可按需加入亲密关系协议，但不强行加入 `crossframe-public`。
- 必须先有结构洞察底稿。
- 正文声口默认是现代编辑底色，不能只输出诊断提纲或概念说明。

## 2. 公共评论

Prompt：写一篇“平台申诉为什么可能只是表面治理”的公共评论。

期望：

- 工作流包含 `crossframe -> crossframe-public -> crossframe-essay -> crossframe-review`。
- 必须查源或声明需要查源。
- 不能让检索材料接管文章命题。
- 正文用评论体，亲切但能严厉批评表演性治理。

## 3. 组织修复

Prompt：给这个项目失败写组织修复备忘录，再转成一篇给内部看的文章。

期望：

- 工作流包含 `crossframe -> crossframe-org -> crossframe-essay -> crossframe-review`。
- 先输出组织备忘录所需结构，再成文。
- 检查责任链、授权链、反馈写回。

## 4. 答读者问

Prompt：像编辑回信一样回答“是不是我太敏感”。

期望：

- 工作流包含 `crossframe -> crossframe-dialogue -> review-lite`。
- 不默认进入长文。
- 不把修复责任压回提问者。

## 5. 读书后成文

Prompt：读这篇文章，写与 CrossFrame 的关联与不同，并扩成一篇思想文章。

期望：

- 工作流包含 `crossframe -> crossframe-notebook -> crossframe-essay -> crossframe-review`。
- 先比较关联、不同、可吸收处和冲突处，再成文。
- 不伪造引用。

## 6. 辩论后成文

Prompt：先检验“所有制度问题都是反馈问题”这个命题，再写一篇文章。

期望：

- 工作流包含 `crossframe -> crossframe-debate -> crossframe-essay -> crossframe-review`。
- 必须列隐藏前提、最强反驳和撤回条件。
- 文章不能把命题写成绝对真理。

## 7. 只评审

Prompt：评审这段 CrossFrame 输出是否合格。

期望：

- 工作流为 `crossframe-review`。
- 不重跑完整生成链。
- 输出评审对象、事实边界、失败点和修复建议。

## 8. 过度触发失败

Prompt：写一篇普通关系文章。

失败表现：

- 同时读取全部 sibling skill。
- 把案例库、公共制度、组织修复、读书笔记全部列入必读。

期望：

- 只读取必要链路。
- 在“不读取”中说明至少两个未触发 skill。
