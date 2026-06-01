<div align="center">

# CrossFrame Skill

### 让 AI 分析复杂问题时，先想清楚，再说人话。

**适合关系、团队、组织、制度和公共争议里的复杂问题。**

<br>

![许可证](https://img.shields.io/badge/许可证-MIT-f3d7e6?style=flat-square&labelColor=fff7fb&color=f3d7e6)
![用途](https://img.shields.io/badge/用途-复杂问题分析-d8ebff?style=flat-square&labelColor=fafcff&color=d8ebff)
![输出](https://img.shields.io/badge/输出-推理提纲%20%2B%20人话判断-e4ddff?style=flat-square&labelColor=fffaff&color=e4ddff)
![语言](https://img.shields.io/badge/语言-中文为主-f8efcf?style=flat-square&labelColor=fffdf6&color=f8efcf)

<p align="center">
  <a href="#what"><strong>它能做什么</strong></a>
  ·
  <a href="#how"><strong>它怎么回答</strong></a>
  ·
  <a href="#install"><strong>安装方式</strong></a>
  ·
  <a href="#adapters"><strong>其他 AI 软件</strong></a>
  ·
  <a href="skills/crossframe/SKILL.md"><strong>Skill 文件</strong></a>
</p>

</div>

---

## 一句话说明

CrossFrame 是一个给 AI 用的中文 skill。

它的作用很简单：**不要让 AI 一上来就套概念，而是先读取必要概念、把问题拆清楚，再给一个普通人能读懂的判断。**

比如，不要这样回答：

> 这是典型的结构性熵增、主体层不足、回流链断裂。

而是这样回答：

> 这不一定是你不够努力，而是你提出的问题没有改变任何规则、资源或角色。久而久之，你就变成了那个一直替系统吸收成本的人。

---

<a id="what"></a>
## 它能做什么？

CrossFrame 适合这类问题：

- 一段关系里，为什么总是一个人在解释、道歉、补救？
- 一个团队为什么每次复盘都说得对，下一轮还是一样？
- 一个项目为什么越推进越累，真实反馈越来越少？
- 一个组织为什么有流程，却没有真正的申诉和纠错能力？
- 一个公共争议为什么越讨论越像站队，越难看见事实？
- 证据还不够，但事情已经很紧急，下一步能做什么小动作？

它不负责替你做人格审判，也不负责给世界下最终判决。

它更像一个分析助手：先帮你分清事实、猜测、责任、风险和下一步。

---

<a id="how"></a>
## 它怎么回答？

默认情况下，它会先给一个很短的推理提纲。

```text
推理提纲
- 诊断对象：我们这次到底在分析什么
- 事实边界：哪些是已知事实，哪些还只是猜测
- 尺度窗口：这是个人问题、关系问题，还是组织/制度问题
- 机制候选：至少列出两种可能原因
- 判断档位：现在能不能下强判断，还是只能暂时判断
- 下一步：接下来观察什么，或者做什么低风险动作
```

然后再给正式回答。

这样做的好处是：你能看出来 AI 有没有真的推理，而不是直接把一串概念扔出来。

它现在还会多做一步：如果回答里要用到容易失真的概念，比如“承接”“回流”“开放断言”“证据成本”“退出转移”“爱”，它会先读取对应概念卡，再输出判断。这样不是把原文整篇塞进去，而是在需要的时候补足关键概念。

---

## 它特别强调什么？

### 1. 先说人话

第一段要让没读过任何框架的人也能明白。

术语可以有，但只能放在后面解释，不能拿来冒充结论。

### 2. 先吸收必要概念

CrossFrame 不再依赖“把一整篇原文塞给 AI”。它会按问题类型读取对应的概念卡、证据规则和判断档位规则。

这样既保留 v2.0 的关键概念，又不让输出变成一堵术语墙。

### 3. 不急着定性别人

复杂问题里，最容易犯的错就是把结构问题说成某个人“就是坏”“就是没救”“就是没有主体性”。

CrossFrame 会先问：到底是什么流程、关系、责任分配或反馈机制出了问题。

### 4. 判断要能撤回

如果证据还不够，它不会装作已经看透一切。

它会说明：现在这个判断基于什么；如果出现什么新事实，这个判断应该被修改。

### 5. 高风险场景要更谨慎

如果事情涉及处分、名誉、权利、资源、组织权力或公共评价，它会额外检查：

- 信息是不是被一方掌握
- 弱者说真话会不会受惩罚
- 流程是不是只是表面存在
- AI 的漂亮文本是不是被拿来当合规证明

---

## 一个小例子

用户问：

> 我们团队每次复盘都能说出问题，但下一轮还是一样。中层越来越累，基层觉得没人听。

CrossFrame 不应该只说：

> 这是反馈写回失败。

它应该更像这样：

```text
推理提纲
- 诊断对象：团队复盘为什么没有变成真实修复。
- 事实边界：能确定的是复盘很多、下一轮仍重复、中层疲惫、基层觉得没人听。
- 机制候选：一是反馈没有改变规则和资源；二是中层承担了太多翻译和补救成本。
- 判断档位：暂时判断，不做人格定性。
- 下一步：选一个重复问题，看它能不能写进负责人、资源或时间表。
```

正式回答会先说：

> 这个团队不一定缺少反思，真正缺的可能是“说出来以后有没有改变”。如果复盘只增加会议和解释成本，却不改变资源、角色和时间表，大家就会慢慢学会沉默。

---

<a id="install"></a>
## 安装方式

### Codex 安装

```powershell
py -3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo xixilove486/crossframe-skill --path skills/crossframe
```

安装后，本地 Codex 应显示：

```text
crossframe
```

### 手动安装

```powershell
git clone https://github.com/xixilove486/crossframe-skill.git
Copy-Item -Path ".\crossframe-skill\skills\crossframe" -Destination "$HOME\.codex\skills\crossframe" -Recurse -Force
```

### 仓库内快速安装

```powershell
.\scripts\install-codex.ps1
```

---

<a id="adapters"></a>
## 其他 AI 软件

这个仓库也放了几个薄适配文件，方便在其他 AI 工具里使用同一套方法。

| 工具 | 入口文件 |
| --- | --- |
| Codex | `skills/crossframe/` |
| Claude Code | `CLAUDE.md`、`.claude/skills/crossframe/SKILL.md`、`.claude/commands/crossframe.md` |
| Cursor | `.cursor/rules/crossframe.mdc`、`AGENTS.md` |
| Gemini CLI | `GEMINI.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| 通用 agent | `AGENTS.md` |

这些文件只是入口说明。真正的 skill 内容仍然在：

```text
skills/crossframe/
```

更多说明见 [INTERFACES.md](INTERFACES.md)。

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
│     ├─ evals/
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
