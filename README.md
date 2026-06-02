<div align="center">

# CrossFrame Skill Suite

### 让 AI 分析复杂问题时，先想清楚，再说人话；写文章时，先有洞察底稿，再成文。

**适合复杂问题分析，也适合把结构判断写成有批判性洞察力的中文文章。**

<br>

![许可证](https://img.shields.io/badge/许可证-MIT-f3d7e6?style=flat-square&labelColor=fff7fb&color=f3d7e6)
![用途](https://img.shields.io/badge/用途-复杂问题分析-d8ebff?style=flat-square&labelColor=fafcff&color=d8ebff)
![输出](https://img.shields.io/badge/输出-推理提纲%20%2B%20人话判断-e4ddff?style=flat-square&labelColor=fffaff&color=e4ddff)
![文章](https://img.shields.io/badge/文章-洞察底稿%20%2B%20正文-d9f2df?style=flat-square&labelColor=fbfffb&color=d9f2df)
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
  ·
  <a href="skills/crossframe-essay/SKILL.md"><strong>Essay Skill</strong></a>
</p>

</div>

---

## 一句话说明

CrossFrame 是一组给 AI 用的中文 skills。

它们的作用很简单：**不要让 AI 一上来就套概念，而是先读取必要概念、把问题拆清楚，再给一个普通人能读懂的判断或文章。**

仓库里现在有两个平行 skill：

- `crossframe`：用于结构诊断、推演、开放断言、反俘获和低条件行动。
- `crossframe-essay`：用于写中文批判性洞察文章，默认先给 `结构洞察底稿`，再给 `文章正文`；需要深度时可按需概念上升、引入中西经典或理论参照。

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

CrossFrame Essay 适合这类写作：

- 写一篇“团队越复盘越失真”的组织洞察文章。
- 写一篇“解释劳动为什么会耗竭”的关系文章。
- 写一篇“平台申诉为什么可能只是表面治理”的公共议题评论。
- 写一篇“生命第一因”的思想文章，但先拆清科学起源、结构定义和意义问题。
- 把零散素材整理成一篇有递进、有边界、不堆术语的长文。

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

对更复杂的场景，它会进入更深的后台模块：强判断要做命题验证，高反身对象要区分诊断前后反应，亲密关系要先保护痛苦和边界，疗愈场景要区分抢救、修复、重建和退出转移，公共制度要检查证据通道、申诉有效性和低权力主体保护。

这一版还补了 v2.0 里更容易失真的深水区：什么时候不能把 CrossFrame 当万能理论，长期演化怎么判断阶段，忙了很久为什么没有积累，什么时候退出不是逃避，公共承诺为什么必须有偿付，宏大判断哪里必须承认可判断边界。普通输出不会把这些术语全倒出来，它们主要在后台帮助 AI 不乱判。

写文章时，`crossframe-essay` 会多做一步：先把判断整理成一份 `结构洞察底稿`，包括事实边界、机制候选、责任链、成本链、证据缺口和文章递进顺序；然后才写正文。这样文章不是靠气势推进，而是有一个能回头检查的判断底座。

如果文章需要更深，它还会再加一层：从现实机制里抽象出上位概念，再选择贴切的经典、理论、历史经验或文学互文，最后回到现实责任链。它不会为了显得高级而堆名人名言；直接引用必须能核验，不确定原句时只做意译或思想映射。

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

### 6. 深水区按需读取

不是每个问题都需要完整理论。只有当问题进入强判断、高反身性、亲密关系、疗愈转移、公共制度或长期演化时，CrossFrame 才读取对应后台模块。

这让它保留 v2.0 的深度，但不会把普通回答写成理论论文。

### 7. 不把框架当万能钥匙

CrossFrame 可以帮你看结构，但不能替代法律、医疗、工程、安全等专业判断，也不能拿来给某个人做最终人格定性。

如果用户想用它“证明某人就是有问题”，或者想把 AI 生成报告当成合规证据，它会先停下来检查边界。

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
py -3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo xixilove486/crossframe-skill --path skills/crossframe-essay
```

安装后，本地 Codex 应显示：

```text
crossframe
crossframe-essay
```

### 手动安装

```powershell
git clone https://github.com/xixilove486/crossframe-skill.git
Copy-Item -Path ".\crossframe-skill\skills\crossframe" -Destination "$HOME\.codex\skills\crossframe" -Recurse -Force
Copy-Item -Path ".\crossframe-skill\skills\crossframe-essay" -Destination "$HOME\.codex\skills\crossframe-essay" -Recurse -Force
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
| Codex | `skills/crossframe/`、`skills/crossframe-essay/` |
| Claude Code | `CLAUDE.md`、`.claude/skills/crossframe*/SKILL.md`、`.claude/commands/crossframe*.md` |
| Cursor | `.cursor/rules/crossframe.mdc`、`.cursor/rules/crossframe-essay.mdc`、`AGENTS.md` |
| Gemini CLI | `GEMINI.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Windsurf / Cascade | `.windsurf/rules/crossframe.md`、`AGENTS.md` |
| Cline | `.clinerules/crossframe.md` |
| Roo Code | `.roo/rules/crossframe.md` |
| Continue | `.continue/rules/crossframe.md` |
| Aider | `CONVENTIONS.md`、`.aider.conf.yml` |
| LLM 索引 | `llms.txt` |
| 通用 agent | `AGENTS.md` |

这些文件只是入口说明。真正的 skill 内容仍然在：

```text
skills/crossframe/
skills/crossframe-essay/
```

更多说明见 [INTERFACES.md](INTERFACES.md)。

---

## 仓库结构

```text
crossframe-skill/
├─ skills/
│  ├─ crossframe/
│  │  ├─ SKILL.md
│  │  ├─ protocols/
│  │  ├─ worksheets/
│  │  ├─ references/
│  │  ├─ templates/
│  │  ├─ evals/
│  │  └─ examples/
│  └─ crossframe-essay/
│     ├─ SKILL.md
│     ├─ protocols/
│     ├─ references/
│     ├─ templates/
│     ├─ evals/
│     └─ examples/
├─ .claude/
├─ .clinerules/
├─ .continue/
├─ .cursor/
├─ .github/
├─ .roo/
├─ .windsurf/
├─ scripts/
├─ AGENTS.md
├─ CLAUDE.md
├─ CONVENTIONS.md
├─ GEMINI.md
├─ INTERFACES.md
├─ llms.txt
└─ README.md
```

其中 `skills/crossframe/references/v2-coverage-map.md` 记录了 v2.0 各个重要模块在 skill 里的对应位置。它不是给普通用户看的理论书，而是防止维护时漏掉关键概念。

## 许可

MIT License. See [LICENSE](LICENSE).
