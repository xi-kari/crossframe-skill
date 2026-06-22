const demos = {
  philosophy: {
    input: "/crossframe-suite 2+1，一个问题什么时候不该被直接回答？",
    workflow: "crossframe -> crossframe-essay -> crossframe-review -> crossframe-inquiry",
    output: [
      "拆成事实问题、概念问题和意义问题。",
      "判断哪些部分可以回答，哪些只能保留为开放断言。",
      "把“回答问题”转成“澄清问题结构”的过程。"
    ],
    review: "如果正文把开放断言写成终局答案，review 会要求降档或重写。",
    inquiry: "继续追问：这个问题是为了得到结论，还是为了制造一个更好的思考靶点？"
  },
  history: {
    input: "/crossframe-suite 分析一个虚构城邦从扩张到停滞的结构原因",
    workflow: "crossframe -> crossframe-history -> crossframe-essay -> crossframe-review",
    output: [
      "进入 history skill，标记历史草稿档或历史接口分析档。",
      "区分来源族、具体史料、断代边界和历史因果降级。",
      "避免把复杂历史写成单一原因或宿命叙事。"
    ],
    review: "如果来源族被写成完整史料闭包，review 会要求补 source_id 或降档。",
    inquiry: "继续追问：哪些阶段解释需要分开，哪些结论只能保留为机制候选？"
  },
  org: {
    input: "/crossframe-suite 为什么一个虚构团队反复复盘，却没有真实改变？",
    workflow: "crossframe -> crossframe-org -> crossframe-essay -> crossframe-review",
    output: [
      "检查授权链、责任链、反馈写回和停止条件。",
      "防止把结构问题压成“态度不好”或“执行力不足”。",
      "给出低风险试点，而不是直接组织处置。"
    ],
    review: "如果行动建议超过授权条件，review 会限制 action_ceiling。",
    inquiry: "继续追问：最小可试的反馈写回是什么，什么迹象说明应停止试点？"
  },
  public: {
    input: "/crossframe-suite 一个虚构平台有申诉入口，能否证明治理有效？",
    workflow: "crossframe -> crossframe-public -> crossframe-essay -> crossframe-review",
    output: [
      "区分入口存在、流程可用、责任可追和救济有效。",
      "检查公共承诺与可验证证据的差距。",
      "给出可发布边界和需要补证的位置。"
    ],
    review: "如果把“入口可见”写成“治理有效”，review 会标记为正文强于台账。",
    inquiry: "继续追问：还需要哪些 source_id 才能支撑更高档位的公共判断？"
  },
  inquiry: {
    input: "刚才那篇匿名结构分析，还能往哪儿追问？",
    workflow: "previous context -> crossframe-inquiry",
    output: [
      "复用上游 claim ledger、source ledger 和 review warning。",
      "定向检索 1-3 个相关 sibling skill 的必要材料。",
      "提出反证、补证、迁移和收束问题。"
    ],
    review: "如果用户只是谢谢、好的、明白了或先这样，不展开 inquiry。",
    inquiry: "继续追问：哪条中心命题最脆弱，哪条行动建议最容易越界？"
  }
};

const installs = {
  codex: `git clone https://github.com/xi-kari/crossframe-skill
cd crossframe-skill
.\\scripts\\install-codex.ps1

# Start with:
/crossframe-suite 分析这个团队为什么复盘很多但没有真实修复`,
  claude: `Copy into your project:

.claude/skills/crossframe*
.claude/commands/crossframe*.md
CLAUDE.md

# Then use:
/crossframe-suite
/crossframe-essay
/crossframe-review
/crossframe-inquiry`,
  agents: `Read these thin adapters first:

AGENTS.md
CLAUDE.md
GEMINI.md
llms.txt
docs/ADAPTERS.md

Keep the canonical skill bodies in:
skills/crossframe*/`
};

function setDemo(key) {
  const demo = demos[key];
  if (!demo) return;

  document.querySelectorAll(".demo-tab").forEach((button) => {
    const active = button.dataset.demo === key;
    button.classList.toggle("is-active", active);
    button.setAttribute("aria-selected", String(active));
  });

  document.getElementById("demo-input").textContent = demo.input;
  document.getElementById("demo-workflow").textContent = demo.workflow;
  document.getElementById("demo-review").textContent = demo.review;
  document.getElementById("demo-inquiry").textContent = demo.inquiry;

  const output = document.getElementById("demo-output");
  output.replaceChildren(
    ...demo.output.map((item) => {
      const li = document.createElement("li");
      li.textContent = item;
      return li;
    })
  );
}

function setInstall(key) {
  const code = installs[key];
  if (!code) return;

  document.querySelectorAll(".install-tab").forEach((button) => {
    const active = button.dataset.install === key;
    button.classList.toggle("is-active", active);
    button.setAttribute("aria-selected", String(active));
  });

  document.getElementById("install-code").textContent = code;
}

document.querySelectorAll(".demo-tab").forEach((button) => {
  button.addEventListener("click", () => setDemo(button.dataset.demo));
});

document.querySelectorAll(".install-tab").forEach((button) => {
  button.addEventListener("click", () => setInstall(button.dataset.install));
});

setDemo("philosophy");
setInstall("codex");
