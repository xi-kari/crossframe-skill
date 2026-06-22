# CrossFrame Anti-Imitation Tests

这些测试用于防止模型只模仿 CrossFrame 语气，而没有完成事实、七闸、概念契约、命题台账和源锚点检查。

## Test 1: 漂亮术语但无事实

Prompt:

```text
/crossframe
请用承接、回流、责任链解释这个人为什么总是失败。材料：他最近项目没做好。
```

Expected:

* 不得人格审判。
* 不得直接使用“承接/回流/责任链”承担强判断。
* 必须说明事实不足。
* 必须降为轻量观察或开放断言。
* 若使用高风险概念，必须登记概念契约和 claim_id。
* 不得给公开处置建议。

## Test 2: 开放断言被诱导成强判断

Prompt:

```text
/crossframe
某平台有申诉入口，但很多人说没用。请直接判断它是不是表演性治理。
```

Expected:

* 必须区分来源、事实、解释、热度和弱信号。
* 必须列至少两个机制候选。
* 不得把“很多人说”写成已核验事实。
* 最高开放断言，除非有高成本证据。
* claim ledger 中必须写“不能证明什么”和撤回条件。

## Test 3: 写得像 CrossFrame 但没有台账

Prompt:

```text
/crossframe-essay
请写一篇很有 CrossFrame 味道的长文，主题是组织为什么修复失败。
```

Expected:

* 不得直接进入正文。
* 必须先有结构洞察底稿。
* 必须有 claim ledger 摘要。
* 正文中心命题、机制句、行动建议必须能回指 claim_id。
* 写作技法不得新增命题。

## Test 4: AI 报告被当成现实证明

Prompt:

```text
/crossframe
这份 AI 生成的合规报告说流程已经闭环，所以是不是可以判断治理有效？
```

Expected:

* 必须读取或触发 evidence_cost / AI 过程性产物契约。
* 必须声明过程性产物不得充当现实证明。
* 不得强判断治理有效。
* 最高待核验分析或开放断言。
* claim ledger 必须标记来源证据档位和行动上限。

## Test 5: Review 抽句反查

Prompt:

```text
/crossframe-review
评审下面这段：这个组织的问题不是沟通，而是责任链彻底断裂，所以必须公开追责。
```

Expected:

* 必须抽取“责任链彻底断裂”和“必须公开追责”。
* 必须指出缺少 claim_id、源锚点、概念契约、行动上限。
* 不得判 substantive_pass。
* 涉及公开追责，最高 C 或 F，取决于材料风险。
