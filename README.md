<div align="center">

# CrossFrame Skill

### 跨尺度结构诊断框架 v2.0 的推理协议型 skill

**不是把概念塞进上下文，而是先形成推理提纲，再输出可撤回、可行动的判断。**

<br>

![许可证](https://img.shields.io/badge/许可证-MIT-f3d7e6?style=flat-square&labelColor=fff7fb&color=f3d7e6)
![技能类型](https://img.shields.io/badge/技能-结构诊断协议-d8ebff?style=flat-square&labelColor=fafcff&color=d8ebff)
![关注重点](https://img.shields.io/badge/重点-证据闸%20%7C%20机制候选%20%7C%20开放断言-e4ddff?style=flat-square&labelColor=fffaff&color=e4ddff)
![语言](https://img.shields.io/badge/语义-中文为准-f8efcf?style=flat-square&labelColor=fffdf6&color=f8efcf)

<p align="center">
  <a href="#why"><strong>为什么需要</strong></a>
  ·
  <a href="#what"><strong>能做什么</strong></a>
  ·
  <a href="#workflow"><strong>推理流程</strong></a>
  ·
  <a href="#install"><strong>安装方式</strong></a>
  ·
  <a href="#adapters"><strong>其他接口</strong></a>
  ·
  <a href="skills/crossframe/SKILL.md"><strong>Skill 入口</strong></a>
</p>

</div>

---

> [!IMPORTANT]
> **CrossFrame** 是“跨尺度结构诊断框架”的英文传播名与 skill id。  
> 框架的权威语义仍然是中文：承接、回流、开放断言、责任链、观测反身性、低条件试探行动、退出转移、不浪费爱。

<a id="why"></a>
## 为什么需要这个 skill？

很多结构分析会失败，不是因为没有概念，而是因为太快跳到了概念。

常见坏输出是：

> 这是典型的结构性熵增，说明主体层不足，回流链断裂。

它听起来像在分析，实际上可能没有做三件最基本的事：

- 没有界定正在诊断的对象
- 没有区分事实、解释和猜测
- 没有比较至少两个机制候选
- 没有说明判断能被什么证据撤回
- 没有把术语翻译成普通人能用的现实语言

CrossFrame 的目标，就是把 v2.0 从“提示词工程”改造成一个**可执行的推理协议**。

---

<a id="what"></a>
## 这个 skill 能做什么？

CrossFrame 适合分析复杂人类系统里的失衡、修复与判断边界，例如：

- 一段关系为什么总是一个人在解释、补救、承接
- 一个团队为什么复盘很多，却没有真实改变
- 一个组织为什么有流程，却没有真实申诉能力
- 一个公共议题为什么越讨论越被标签化
- 一个系统是否已经进入权力封闭，需要退出转移
- 证据不足但风险紧急时，下一步能不能做低条件试探行动

它不是人格审判器，也不是世界真理机器。

它更像一个诊断工作台：先把对象、事实、尺度、责任链和观测影响摆出来，再决定这次只能做轻量观察、开放断言、完整诊断、强判断、低条件行动，还是退出转移。

---

<a id="workflow"></a>
## 核心推理流程

默认输出前，CrossFrame 会先给一个可见的**推理提纲**：

```text
推理提纲
- 诊断对象：
- 事实边界：
- 尺度窗口：
- 机制候选：
- 判断档位：
- 下一步：
```

随后才进入正式输出。

内部必须执行：

1. 判断用户请求类型：诊断、推演、开放断言、低条件行动、高责任审查或概念解释。
2. 填写 intake：对象、尺度、事实、证据缺口、用途、受影响对象。
3. 通过五闸：对象闸、证据闸、尺度闸、责任闸、观测闸。
4. 形成至少两个机制候选。
5. 决定判断档位。
6. 先说人话，再按需补内部映射。

---

## 说人话原则

CrossFrame 明确要求：默认先说人话，不堆术语。

- 第一段必须让没读过框架的人也能明白。
- 术语只能作为附加映射，不能当结论本身。
- 删除所有框架术语后，核心判断仍然必须成立。
- 不用“这是典型的某某概念，所以……”替代推理。

好的表达应像这样：

> 这不一定是你不够努力，而是你的反馈没有改变任何规则、资源或角色，所以你越来越像在替系统吸收成本。

---

<a id="install"></a>
## 安装方式

### Codex 安装（推荐）

使用 Codex 自带的 `skill-installer`，直接从 GitHub 安装：

```powershell
py -3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo xixilove486/crossframe-skill --path skills/crossframe
```

安装后，本地 Codex 应显示 skill id：

```text
crossframe
```

### 手动安装

```powershell
git clone https://github.com/xixilove486/crossframe-skill.git
Copy-Item -Path ".\crossframe-skill\skills\crossframe" -Destination "$HOME\.codex\skills\crossframe" -Recurse -Force
```

### 本仓库内快速安装脚本

```powershell
.\scripts\install-codex.ps1
```

---

<a id="adapters"></a>
## 其他 AI 软件适配

这个仓库除了 Codex skill 主体，也提供薄适配层。它们不复制完整正文，只负责让不同工具知道应该读取哪里。

| 接口 | 入口文件 | 用法 |
| --- | --- | --- |
| Codex | `skills/crossframe/` | 推荐安装路径 |
| Claude Code | `CLAUDE.md`、`.claude/skills/crossframe/SKILL.md`、`.claude/commands/crossframe.md` | 打开仓库后可用 `/crossframe ...` |
| Gemini CLI | `GEMINI.md` | 仓库级上下文入口 |
| Cursor | `.cursor/rules/crossframe.mdc`、`AGENTS.md` | 作为规则或通用 agent 入口 |
| GitHub Copilot | `.github/copilot-instructions.md` | 仓库级 Copilot 说明 |
| 通用 agent | `AGENTS.md` | 非特定厂商默认入口 |

详细说明见 [INTERFACES.md](INTERFACES.md)。

---

## 仓库结构

```text
crossframe-skill/
├─ skills/
│  └─ crossframe/
│     ├─ SKILL.md
│     ├─ protocols/
│     ├─ worksheets/
│     ├─ references/
│     ├─ templates/
│     └─ examples/
├─ .claude/
├─ .cursor/
├─ .github/
├─ scripts/
├─ AGENTS.md
├─ CLAUDE.md
├─ GEMINI.md
├─ INTERFACES.md
└─ README.md
```

## 许可

MIT License. See [LICENSE](LICENSE).
