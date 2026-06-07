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
  <a href="skills/crossframe-suite/SKILL.md"><strong>Suite 总入口</strong></a>
  ·
  <a href="skills/crossframe/SKILL.md"><strong>Skill 文件</strong></a>
  ·
  <a href="skills/crossframe-essay/SKILL.md"><strong>Essay Skill</strong></a>
  ·
  <a href="skills/crossframe-critical/SKILL.md"><strong>Critical Skill</strong></a>
</p>

</div>

---

## 一句话说明

CrossFrame 是一组给 AI 用的中文 skills。整套 skill 只能显式触发：用户必须点名 `crossframe-suite`、`crossframe`、某个 `crossframe-*`，或使用对应命令；不要因普通分析、写作、评论、组织修复、读书或辩论任务被动触发。

它们的作用很简单：**不要让 AI 一上来就套概念，而是先读取必要概念、把问题拆清楚，再给一个普通人能读懂的判断或文章。**

这一版又补了一层“3.0 源结构连续性”：CrossFrame 不把 `跨尺度结构诊断框架v3.0.docx` 整篇粗暴塞进上下文，但会保存它的章节脊柱、逐节摘要和必须联读的连续板块。这样拆成 skill 以后，AI 不会只读一张概念卡就下判断。

显式调用之后，仓库里这组平行 skill 仍然可以由 `crossframe-suite` 调度。`suite` 显式启动后的内部联合调用不算被动触发：

- `crossframe-suite`：显式调用后的推荐总入口，用于判断一个任务应该连续读取哪些 sibling skill，以及按什么顺序执行。只要从总入口进入，默认最终都输出 `full-visible-v3-longform / 3.0混合长文`：完整可见底稿 + 完整长文正文；评审、案例库、备忘录、表格或行动清单会先做，再默认转成文章，除非你明确说“只要/不要文章/短答”。
- `crossframe`：用于结构诊断、推演、开放断言、反俘获和低条件行动。
- `crossframe-essay`：用于写中文批判性洞察文章，默认先给完整可见 `结构洞察底稿`，再给 1200-2200 中文字的完整 `文章正文`；自动成文默认带现代编辑底色，像一位耐心、谦逊、认真、果敢的编辑回应读者问题；需要深度时可按需概念上升、引入中西经典或理论参照。
- `crossframe-critical`：用于**点名调用**的结构批判长文。它先按 CrossFrame 做事实边界、尺度窗口、机制候选和判断档位，再进入更锋利的批判矩阵：成本链、受益链、权力/资源分配、概念遮蔽、再生产机制、弱信号和撤回条件。默认输出 `批判底稿 + 篇章方案 + 1800-2800 中文字正文`，并要求现实例子。它不接入 `crossframe-suite` 总调用，只有你明确写 `$crossframe-critical` 或点名时才用。
- `crossframe-review`：用于审查输出有没有真的推理，抓概念堆砌、伪推理、证据边界缺失和跳过底稿。
- `crossframe-dialogue`：用于答读者问、编辑回信和咨询式短答复。
- `crossframe-casebook`：用于把聊天记录、组织材料、项目复盘和公共争议整理成可复用案例库。
- `crossframe-public`：用于公共议题、平台申诉、制度评论和合规材料的证据边界诊断。
- `crossframe-org`：用于团队、项目、组织修复，输出备忘录、反馈写回方案、复盘改造和低风险试点。
- `crossframe-teach`：用于把 CrossFrame 概念讲给普通人，带误读边界、现实信号和练习。
- `crossframe-debate`：用于把命题拆成正反结构、隐藏前提、证据要求和撤回条件。
- `crossframe-notebook`：用于读书、理论和文章研究笔记，强调与 CrossFrame 的关联、不同、冲突和可吸收处。

## 每个 skill 做什么？

| Skill | 主要功能 | 默认输出 | 显式触发方式 |
| --- | --- | --- | --- |
| `crossframe-suite` | 总入口，决定连续读取哪些 skill，以及哪些不读取。 | 调度提纲 + 专项产物 + `3.0混合长文`；任何内容任务默认追加完整文章层。 | 用户明确点名 `crossframe-suite`、`$crossframe-suite`、`/crossframe-suite` 或要求使用 CrossFrame Suite。 |
| `crossframe` | 做结构诊断，先分清事实、尺度、证据、责任和机制候选。 | 推理提纲 + 人话判断 / 开放断言 / 推演 / 低条件行动。 | 用户明确点名 `crossframe`、`$crossframe`、`/crossframe`、CrossFrame 或跨尺度结构诊断。 |
| `crossframe-essay` | 把结构判断写成中文批判性洞察文章。 | 完整可见结构洞察底稿 + 完整长文正文。 | 用户明确点名 `crossframe-essay`、`$crossframe-essay`、`/crossframe-essay` 或 CrossFrame Essay。 |
| `crossframe-critical` | 点名调用的结构批判长文，先做 CrossFrame 底稿，再用批判矩阵写文章。 | 批判底稿 + 篇章方案 + 1800-2800 字正文。 | 只能明确点名 `$crossframe-critical`、`crossframe-critical` 或要求测试批判 skill；不进入 `crossframe-suite` 默认调度。 |
| `crossframe-review` | 审查输出有没有真的推理。 | 评审报告 / 是否合格 / 修复建议。 | 用户明确点名 `crossframe-review`、`$crossframe-review`、`/crossframe-review` 或 CrossFrame Review。 |
| `crossframe-dialogue` | 写短而有洞察的答复。 | 编辑回信 / 咨询式短答复 / 意见回复。 | 用户明确点名 `crossframe-dialogue`、`$crossframe-dialogue`、`/crossframe-dialogue` 或 CrossFrame Dialogue。 |
| `crossframe-casebook` | 把材料整理成可复用案例。 | 案例库条目 / 案例索引 / 脱敏来源台账。 | 用户明确点名 `crossframe-casebook`、`$crossframe-casebook`、`/crossframe-casebook` 或 CrossFrame Casebook。 |
| `crossframe-public` | 分析公共议题和制度问题的证据边界。 | 公共议题诊断 / 证据边界摘要 / 公共评论底稿。 | 用户明确点名 `crossframe-public`、`$crossframe-public`、`/crossframe-public` 或 CrossFrame Public。 |
| `crossframe-org` | 做团队、项目、组织修复专项。 | 组织诊断备忘录 / 反馈写回方案 / 复盘改造建议 / 低风险试点。 | 用户明确点名 `crossframe-org`、`$crossframe-org`、`/crossframe-org` 或 CrossFrame Org。 |
| `crossframe-teach` | 把 CrossFrame 概念讲给普通人。 | 概念课 / 误读边界 / 现实信号 / 小练习。 | 用户明确点名 `crossframe-teach`、`$crossframe-teach`、`/crossframe-teach` 或 CrossFrame Teach。 |
| `crossframe-debate` | 检验一个命题或争论。 | 正反方结构 / 隐藏前提 / 最强反驳 / 撤回条件。 | 用户明确点名 `crossframe-debate`、`$crossframe-debate`、`/crossframe-debate` 或 CrossFrame Debate。 |
| `crossframe-notebook` | 做读书、理论、文章研究笔记。 | 研究笔记 / 来源台账 / 关联与不同 / 可吸收与冲突处。 | 用户明确点名 `crossframe-notebook`、`$crossframe-notebook`、`/crossframe-notebook` 或 CrossFrame Notebook。 |

最简单的记法：**只有显式点名才启动；显式启动后，复杂任务用 `crossframe-suite`，只要某个固定产物时才直接点名对应专项 skill。**

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
- 用亲切的编辑同志口吻，回答“为什么我总是在关系里解释到筋疲力尽”。
- 把零散素材整理成一篇有递进、有边界、不堆术语的长文。

很多时候你不用特意说“请生成文章”。如果你从 `crossframe-suite` 进入，不管是分析、评审、案例、组织修复、概念教学还是命题辩论，它都会默认在必要专项产物之后走文章链路：先诊断或完成专项判断，再生成完整可见 `结构洞察底稿`，最后写成完整长文正文。

其它平行 skill 适合这类任务：

- “写公共评论文章，顺便检查输出质量。” -> `crossframe-suite`
- “用更强批判色彩写一篇结构批判文章，先给底稿和篇章方案。” -> `$crossframe-critical`
- “帮我评审这段 CrossFrame 输出是否合格。” -> `crossframe-review`
- “像编辑回信一样回答这个读者问题。” -> `crossframe-dialogue`
- “把这些聊天记录整理成案例库。” -> `crossframe-casebook`
- “分析这个平台申诉机制是否只是表面治理。” -> `crossframe-public`
- “给这个项目失败写组织修复备忘录。” -> `crossframe-org`
- “把开放断言讲给普通人听，并给练习。” -> `crossframe-teach`
- “检验这个命题的正反双方和撤回条件。” -> `crossframe-debate`
- “读这篇文章，写与 CrossFrame 的关联与不同。” -> `crossframe-notebook`

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

如果使用 `crossframe-suite`，它还会先给一个更短的 `调度提纲`：本次走哪些 skill、哪些不走、最后是否过评审。总入口默认会在必要专项 skill 后进入 `crossframe-essay`，输出档位是 `full-visible-v3-longform / 3.0混合长文`。

这样做的好处是：你能看出来 AI 有没有真的推理，而不是直接把一串概念扔出来。

它现在还会多做一步：如果回答里要用到容易失真的概念，比如“承接”“回流”“开放断言”“证据成本”“退出转移”“爱”，它会先读取对应概念卡，再输出判断。这样不是把原文整篇塞进去，而是在需要的时候补足关键概念。

对更复杂的场景，它会进入更深的后台模块：强判断要做命题验证，高反身对象要区分诊断前后反应，亲密关系要先保护痛苦和边界，疗愈场景要区分抢救、修复、重建和退出转移，公共制度要检查证据通道、申诉有效性和低权力主体保护。

这一版还补了 v3.0 里更容易失真的深水区：什么时候不能把 CrossFrame 当万能理论，长期演化怎么判断阶段，忙了很久为什么没有积累，什么时候退出不是逃避，公共承诺为什么必须有偿付，宏大判断哪里必须承认可判断边界。普通输出不会把这些术语全倒出来，它们主要在后台帮助 AI 不乱判。

写文章时，`crossframe-essay` 会多做一步：先把判断整理成一份完整可见的 `结构洞察底稿`，包括事实边界、机制候选、v3连续联读包、源结构保真、概念风险、责任链、成本链、证据缺口和文章递进顺序；然后才写正文。底稿不能替代正文，正文默认仍是完整长文。

如果一个任务要连续使用多个 skill，`crossframe-suite` 会先给出调度提纲。常见链路是：

```text
普通洞察文章：
crossframe -> crossframe-essay -> crossframe-review

公共评论文章：
crossframe -> crossframe-public -> crossframe-essay -> crossframe-review

组织复盘/修复文章：
crossframe -> crossframe-org -> crossframe-essay -> crossframe-review

答读者问：
crossframe -> crossframe-dialogue -> crossframe-essay(full-visible-v3-longform) -> crossframe-review

读书后成文：
crossframe -> crossframe-notebook -> crossframe-essay -> crossframe-review

辩论后成文：
crossframe -> crossframe-debate -> crossframe-essay -> crossframe-review
```

它不会把所有 skill 一起触发；没用到的 skill 会明确写在“不读取”里，防止上下文变重和判断跑偏。

如果你明确说“只要评审/只要案例库/只要表格/不要文章/短答/纯诊断”，总入口会把这理解为“关闭文章层”，停在你指定的交付物上。否则总入口默认都会让内容更丰富，走完整文章链路。

`crossframe-critical` 是一个例外：它是点名测试用的平行批判 skill，不写入上面的 suite 链路。只有用户明确写 `$crossframe-critical`、`crossframe-critical` 或要求测试这个批判 skill 时才触发。这样可以保留它的锋利度，同时不让默认总调用变成更重的批判模式。

如果文章需要更深，它还会再加一层：从现实机制里抽象出上位概念，再选择贴切的经典、理论、历史经验或文学互文，最后回到现实责任链。它不会为了显得高级而堆名人名言；直接引用必须能核验，不确定原句时只做意译或思想映射。

默认从 `crossframe-suite` 进入并生成文章时，它会进入“现代编辑同志口吻”的底色：先接住读者的困惑，再共同分析结构，必要时严厉批评责任转嫁、伪修复和表演性流程，最后给出清醒、稳妥、有分寸的意见。这里的“同志”不是复古口号，而是一种认真同读者谈问题的姿态。只有你明确要报告、备忘录、表格、清单、纯诊断或学术摘要时，才关闭这种文章声口。

---

## 它特别强调什么？

### 1. 先说人话

第一段要让没读过任何框架的人也能明白。

术语可以有，但只能放在后面解释，不能拿来冒充结论。

### 2. 先吸收必要概念

CrossFrame 不再依赖“把一整篇原文塞给 AI”。它会按问题类型读取对应的概念卡、证据规则和判断档位规则。

这样既保留 v3.0 的关键概念，又不让输出变成一堵术语墙。

### 2.1 不把连续概念拆散

3.0 原文里有些内容是连续展开的，不能拆开读。比如开放断言要和强判断、命题验证、撤回条件一起看；爱要和亲密关系、边界、修复责任一起看；公共制度要和反俘获、弱信号安全、程序有效性一起看。

仓库里现在有三层材料防止读少：

- `v3-source-spine.md`：保存 3.0 DOCX 的章节顺序和相邻关系。
- `v3-section-digest-index.md`：给每节一个保真摘要和误读边界。
- `continuity-bundles.md`：规定哪些概念必须成组读取。

所以 CrossFrame 不是“塞原文”，也不是“只读关键词”。它会先判断当前问题属于哪个连续板块，再按原文结构一起读取必要内容。

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

这让它保留 v3.0 的深度，但不会把普通回答写成理论论文。

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
py -3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo xixilove486/crossframe-skill --path skills/crossframe-suite
py -3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo xixilove486/crossframe-skill --path skills/crossframe
py -3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo xixilove486/crossframe-skill --path skills/crossframe-essay
py -3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo xixilove486/crossframe-skill --path skills/crossframe-critical
py -3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo xixilove486/crossframe-skill --path skills/crossframe-review
py -3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo xixilove486/crossframe-skill --path skills/crossframe-dialogue
py -3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo xixilove486/crossframe-skill --path skills/crossframe-casebook
py -3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo xixilove486/crossframe-skill --path skills/crossframe-public
py -3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo xixilove486/crossframe-skill --path skills/crossframe-org
py -3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo xixilove486/crossframe-skill --path skills/crossframe-teach
py -3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo xixilove486/crossframe-skill --path skills/crossframe-debate
py -3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo xixilove486/crossframe-skill --path skills/crossframe-notebook
```

安装后，本地 Codex 应显示：

```text
crossframe-suite
crossframe
crossframe-essay
crossframe-critical
crossframe-review
crossframe-dialogue
crossframe-casebook
crossframe-public
crossframe-org
crossframe-teach
crossframe-debate
crossframe-notebook
```

### 手动安装

```powershell
git clone https://github.com/xixilove486/crossframe-skill.git
Copy-Item -Path ".\crossframe-skill\skills\crossframe-suite" -Destination "$HOME\.codex\skills\crossframe-suite" -Recurse -Force
Copy-Item -Path ".\crossframe-skill\skills\crossframe" -Destination "$HOME\.codex\skills\crossframe" -Recurse -Force
Copy-Item -Path ".\crossframe-skill\skills\crossframe-essay" -Destination "$HOME\.codex\skills\crossframe-essay" -Recurse -Force
Copy-Item -Path ".\crossframe-skill\skills\crossframe-critical" -Destination "$HOME\.codex\skills\crossframe-critical" -Recurse -Force
Copy-Item -Path ".\crossframe-skill\skills\crossframe-review" -Destination "$HOME\.codex\skills\crossframe-review" -Recurse -Force
Copy-Item -Path ".\crossframe-skill\skills\crossframe-dialogue" -Destination "$HOME\.codex\skills\crossframe-dialogue" -Recurse -Force
Copy-Item -Path ".\crossframe-skill\skills\crossframe-casebook" -Destination "$HOME\.codex\skills\crossframe-casebook" -Recurse -Force
Copy-Item -Path ".\crossframe-skill\skills\crossframe-public" -Destination "$HOME\.codex\skills\crossframe-public" -Recurse -Force
Copy-Item -Path ".\crossframe-skill\skills\crossframe-org" -Destination "$HOME\.codex\skills\crossframe-org" -Recurse -Force
Copy-Item -Path ".\crossframe-skill\skills\crossframe-teach" -Destination "$HOME\.codex\skills\crossframe-teach" -Recurse -Force
Copy-Item -Path ".\crossframe-skill\skills\crossframe-debate" -Destination "$HOME\.codex\skills\crossframe-debate" -Recurse -Force
Copy-Item -Path ".\crossframe-skill\skills\crossframe-notebook" -Destination "$HOME\.codex\skills\crossframe-notebook" -Recurse -Force
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
| Codex | `skills/crossframe*/` 全部可安装 skill |
| Claude Code | `CLAUDE.md`、`.claude/skills/crossframe*/SKILL.md`、`.claude/commands/crossframe*.md` |
| Cursor | `.cursor/rules/crossframe-suite.mdc`、`.cursor/rules/crossframe.mdc`、`.cursor/rules/crossframe-essay.mdc`、`AGENTS.md` |
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
skills/crossframe-suite/
skills/crossframe/
skills/crossframe-essay/
skills/crossframe-critical/
skills/crossframe-review/
skills/crossframe-dialogue/
skills/crossframe-casebook/
skills/crossframe-public/
skills/crossframe-org/
skills/crossframe-teach/
skills/crossframe-debate/
skills/crossframe-notebook/
```

更多说明见 [INTERFACES.md](INTERFACES.md)。

---

## 仓库结构

```text
crossframe-skill/
├─ skills/
│  ├─ crossframe-suite/
│  │  ├─ SKILL.md
│  │  ├─ protocols/
│  │  ├─ references/
│  │  ├─ templates/
│  │  ├─ evals/
│  │  └─ examples/
│  ├─ crossframe/
│  │  ├─ SKILL.md
│  │  ├─ protocols/
│  │  ├─ worksheets/
│  │  ├─ references/
│  │  ├─ templates/
│  │  ├─ evals/
│  │  └─ examples/
│  ├─ crossframe-essay/
│  │  ├─ SKILL.md
│  │  ├─ protocols/
│  │  ├─ references/
│  │  ├─ templates/
│  │  ├─ evals/
│  │  └─ examples/
│  ├─ crossframe-critical/
│  │  ├─ SKILL.md
│  │  ├─ protocols/
│  │  ├─ references/
│  │  └─ templates/
│  └─ crossframe-*/
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

其中 `skills/crossframe/references/v3-coverage-map.md` 记录了 v3.0 各个重要模块在 skill 里的对应位置。它不是给普通用户看的理论书，而是防止维护时漏掉关键概念。

## 许可

MIT License. See [LICENSE](LICENSE).
