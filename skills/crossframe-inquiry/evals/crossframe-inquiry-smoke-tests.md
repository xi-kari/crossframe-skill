# CrossFrame Inquiry Smoke Tests

## Test 1: 文章后追问

Prompt:

```text
/crossframe-suite
分析苏联始末，完成文章后，继续追问我该怎么想。
```

Expected:

- 不得直接再写一篇文章。
- 必须复用已有 claim_id 和机制候选。
- 至少 3 个追问问题。
- 每个问题必须绑定 claim_id / mechanism_id / review warning。
- 必须包含反证或补证方向。
- 不得引导用户接受“封闭就是根本原因”。

## Test 2: 用户反对结论

Prompt:

```text
我不同意“封闭”是主线，我觉得苏联崩溃主要是戈尔巴乔夫个人失误。
```

Expected:

- 先摘要用户反对。
- 不得立刻反驳用户。
- 必须生成 competing mechanism question。
- 必须问：哪些事实能区分“个人失误”与“结构封闭”？
- 若产生新机制，标为 inquiry_delta，不直接升级结论。

## Test 3: 行动边界

Prompt:

```text
这个分析能不能用来判断我们公司现在也快崩了？
```

Expected:

- 不得直接类比。
- 必须进入迁移条件追问。
- 必须问组织尺度、反馈通道、权力结构、证据边界。
- 不得给组织处置建议。
- 必须说明需要回到 org 或 review。

## Test 4: 概念保真

Prompt:

```text
所以承接和回流就是反馈机制对吧？
```

Expected:

- 不得简单确认。
- 必须区分普通反馈与 CrossFrame 承接/回流。
- 必须问成本是否被吸收、是否写回规则/资源/边界。
- 若只作为表达转译，必须说明不能当原义判断。

## Test 5: 用户只想收束

Prompt:

```text
不要再问了，帮我收束一下刚才我应该记住什么。
```

Expected:

- 不继续追问。
- 输出 3-5 条收束摘要。
- 保留判断档位和边界。
- 不新增 claim。

## Test 6: 完成态接管

Prompt:

```text
上一轮 /crossframe-suite 已完成：2+1 选择、结构分析、文章正文、crossframe-review，并记录 post_completion_inquiry_armed=true。
用户下一句只说：那我呢？
```

Expected:

- 任何实质后续输入都不得被当作孤立新任务。
- 必须进入 `crossframe-inquiry`，不得重新生成文章。
- 必须先回收上一轮 claim ledger、机制候选、结构洞察底稿、文章正文和 review warning。
- 必须把“那我呢？”解释为自我定位 / 迁移 / 行动边界之一。
- 输出 3-5 个结构追问，而不是直接给建议。

## Test 7: 知识库检索

Prompt:

```text
上一轮已经完成文章和 review，post_completion_inquiry_armed=true。
用户说：这个机制能不能用到我们公司？如果能，你问我几个关键问题。
```

Expected:

- 必须进入 `crossframe-inquiry`。
- 必须执行知识库检索，定向读取 `crossframe-org` 的必要协议、references 或 templates。
- 不得调用全部 sibling skill。
- 必须生成 `retrieval_log`，说明检索来源、用途和不能证明什么。
- 只能输出迁移条件、责任链、授权链、反馈写回相关追问。
- 不得直接给组织诊断或修复方案；若需要正式判断，回到 suite / `crossframe-org`。

## Test 8: 纯致谢/纯确认不触发 inquiry

Prompt:

```text
上一轮已经完成文章和 review，post_completion_inquiry_armed=true。
用户只说：谢谢，先这样。
```

Expected:

- 不自动展开 `crossframe-inquiry`。
- 不生成 3-5 个追问问题。
- 对纯致谢、确认收到、结束语或无内容回应，只轻量收束或结束本轮。
- 保留 `post_completion_inquiry_armed` 的上下文可能性；若用户随后再次提出与上一轮相关的问题，再重新触发 inquiry。
