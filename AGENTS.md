# CrossFrame / Agent Adapter

本文件是给通用 AI agent 的仓库级入口说明。仓库主体仍以 [README.md](README.md) 与 [skills/crossframe/SKILL.md](skills/crossframe/SKILL.md) 为准。

## 仓库怎么理解

- `skills/crossframe/`：真正可安装的 Codex skill 主体。
- `skills/crossframe/protocols/`：诊断、推演、开放断言、反俘获、低条件行动协议。
- `skills/crossframe/worksheets/`：intake、五闸、证据账本、机制候选等推理发动机。
- `skills/crossframe/templates/`：用户可见输出模板，默认包含推理提纲。
- 适配层：`CLAUDE.md`、`.claude/skills/crossframe/SKILL.md`、`.claude/commands/crossframe.md`、`GEMINI.md`、`.cursor/rules/crossframe.mdc`、`.github/copilot-instructions.md`。

## 何时调用 CrossFrame

当任务涉及以下内容时使用：

- 关系、团队、项目、组织、制度、公共争议中的复杂失衡
- 需要结构诊断、推演、路径展开、后续走向或分支终点
- 需要开放断言，而不是强行给终局判断
- 证据不足但风险紧急，需要低条件试探行动
- 高权力密度、高责任场景，需要反俘获审查
- 用户希望分析复杂反复问题，但不要概念堆砌

不要用于：

- 单纯事实查询
- 代码实现、算术、工具操作等非结构诊断任务
- 医疗、法律、金融等需要专业资质的最终判断
- 用户只是需要安慰，不需要诊断分析的对话

## 必须遵守

1. 中文为权威语义，英文只作传播名或文件名。
2. 先形成内部推理产物，再输出结论。
3. 默认先展示简短推理提纲：
   - 诊断对象
   - 事实边界
   - 尺度窗口
   - 机制候选
   - 判断档位
   - 下一步
4. 先说人话，再按需补术语映射。
5. 至少列两个机制候选，除非证据足以排除其他可能。
6. 不把结构诊断变成人格审判、宿命判断或责任稀释。
7. 开放断言必须包含证据、替代解释、撤回条件和行动边界。

## 读取优先级

1. [skills/crossframe/SKILL.md](skills/crossframe/SKILL.md)
2. 普通诊断读取 `skills/crossframe/protocols/diagnosis-protocol.md`
3. 推演读取 `skills/crossframe/protocols/inference-protocol.md`
4. 开放断言读取 `skills/crossframe/protocols/open-assertion-protocol.md`
5. 高责任场景读取 `skills/crossframe/protocols/anti-capture-protocol.md`
6. 证据不足但紧急读取 `skills/crossframe/protocols/low-condition-action-protocol.md`
7. 输出前读取 `skills/crossframe/templates/reasoning-outline-output.md` 与对应输出模板

## 修改仓库时

- 不要把 `skills/crossframe/` 的可安装入口改丢。
- 不要把薄适配层扩写成另一份完整正文。
- 新增概念前先确认它是否能进入工作表、闸门或模板，否则不要升格。
- 改完后运行 skill 验证，并确认本地安装目录需要同步时已同步。
