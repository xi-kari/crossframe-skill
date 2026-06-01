# GitHub Copilot 仓库指令

- 本仓库主体内容以中文为主；`CrossFrame` 只是英文传播名与 skill id。
- 实际可安装的 Codex skill 位于 `skills/crossframe/`。
- `README.md` 与 `skills/crossframe/SKILL.md` 是原始说明来源；新增适配优先薄封装，不要复制出多套漂移正文。
- 结构诊断、推演、开放断言、反俘获审查或低条件行动任务请遵循 `AGENTS.md`。
- 概念解释或思想解释任务也应进入 CrossFrame，但先读 `skills/crossframe/protocols/concept-explanation-protocol.md`。
- 默认先展示简短推理提纲，再输出普通用户能读懂的判断。
- 输出必须区分事实、解释、机制候选、判断档位和本次读取的概念。
- 高风险概念如承接/回流、开放断言、尺度转移、观测反身性、权力封闭、低条件行动、爱/开放行动、责任链、证据成本、机制候选、判断档位、退出转移、修复副产品，必须先读 `skills/crossframe/references/concept-cards/` 对应卡片。
- 输出前用 `skills/crossframe/worksheets/concept-fidelity-check.md` 避免概念压缩失真。
- 不要把结构诊断变成人格审判、命运预言、责任稀释或概念堆砌。
- 修改仓库时，不要删除 `skills/crossframe/` 的可安装入口。
