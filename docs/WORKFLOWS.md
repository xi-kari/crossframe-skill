# 工作流

## 默认入口

复杂任务优先进入：

```text
crossframe-suite
```

Suite 只负责调度，不替代专项 skill。它会先输出调度提纲，再读取所需 sibling skills。

## 常见链路

| 任务 | 推荐链路 |
| --- | --- |
| 结构诊断 | `crossframe -> crossframe-review` |
| 中文长文 | `crossframe -> crossframe-essay -> crossframe-review` |
| 公共评论 | `crossframe -> crossframe-public -> crossframe-essay -> crossframe-review` |
| 组织复盘 | `crossframe -> crossframe-org -> crossframe-essay -> crossframe-review` |
| 历史研究 | `crossframe -> crossframe-history -> crossframe-essay -> crossframe-review` |
| 答读者问 | `crossframe -> crossframe-dialogue` |
| 读书研究 | `crossframe -> crossframe-notebook` |
| 命题辩论 | `crossframe -> crossframe-debate -> crossframe-review` |
| 完成后追问 | `previous_context -> crossframe-inquiry` |

## 完整长文链路

未显式关闭文章层时，suite 默认形成：

```text
crossframe
-> source-continuity-check
-> v5-read-state-capsule
-> source-anchor-integrity-check
-> claim ledger / claim-ledger-check
-> needed sibling skills
-> crossframe-essay
-> crossframe-review
-> crossframe-inquiry armed
```

完整链路完成后，下一轮用户没有明确说“新任务 / 换主题 / 退出追问 / 不接着上文”时，默认进入 `crossframe-inquiry`。

## 纯追问例外

如果用户已经有上游分析、文章、底稿或 review，又要求“继续追问”“我不同意”“还有别的解释吗”“怎么迁移到我这里”，不要重新默认成文，直接进入 inquiry。缺少上游 `claim ledger` 时，先做轻量 review 或要求用户提供上游输出。
