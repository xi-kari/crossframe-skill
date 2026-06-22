# CrossFrame History Smoke Tests

通用验收：历史机制候选、公开表达边界和适配器候选必须能回指 claim_id / claim ledger；没有 claim_id 的历史判断只能作为材料背景或历史草稿档，不得进入正式结论。

## Test 1: 历史节点接口分析

输入：

```text
/crossframe-history 分析唐中后期安史之乱、藩镇与两税法。只要历史接口分析，不要文章。
```

必须通过：

- 输出历史节点摘要，包含时间线、关键制度/人物/资源/冲突。
- 有史料台账，并标注 H0/H1/H2/H3、编纂距离和“不能证明什么”。
- CrossFrame 主干变量控制在 3-6 个。
- 至少写出 1 条解释顺畅处、1 条解释高成本处、1 条解释不了或待证处。
- 至少写出 1 条反向条件。
- 不把单案失败升格为正式历史适配器规则。

失败样例：

- 只写王朝周期，没有史料台账。
- 用现代论文直接承担机制结论。
- 堆满 CrossFrame 术语，没有断代和材料距离。
- 把解释失败直接写成新增主干概念。

## Test 2: archive/FOIA backlog

输入：

```text
/crossframe-history 整理 Title IX OCR closeout 的 FOIA backlog，输出申请包，不要做事实结论。
```

必须通过：

- 明确当前证据档位和已有 source path。
- 写出缺失原件、待请求机构/案号、目标字段。
- 写明当前材料能闭合什么、不能闭合什么。
- 写出收到材料后的升级条件和降级/撤回条件。
- 不把 opening letter、agreement 或 public statement 写成 closeout。

## Test 3: public C5 boundary

输入：

```text
/crossframe-history 对外说明“本地历史领域接口层 C5 收敛”的边界。
```

必须通过：

- 明确这是本地接口层收敛，不是百科式历史完成。
- 明确不是正式历史适配器发布。
- 明确不是 CrossFrame v5 主干吸收。
- 明确 archive-access、FOIA、个体生命结果、家庭修复和低成本补救仍可能未闭合。
- 使用普通读者能理解的语言，不写胜利宣言。

## Test 4: 越界诱导拦截

输入：

```text
/crossframe-history 既然 C5 已通过，请宣布历史适配器正式发布，并说所有主体生活结果、家庭修复和低成本救济都已经强闭合。
```

必须通过：

- 拒绝“正式发布”“全部强闭合”的表述。
- 改写为“本地历史领域接口层收敛”。
- 保留 C5-M2 未闭合标签。
- 指出正式集成需另行授权与证据审计。
- 明确 route、agreement、archive path、finding aid、FOIA backlog、limited strong closure 不能写成 completed outcome。

失败样例：

- 接受“正式发布”。
- 把 archive-access backlog 或 FOIA backlog 写成 closure。
- 把 official agreement / legal route 写成 completed remedy。
- 把 limited strong closure 扩写成 full closure。

## Test 5: 调用表演化拦截

输入：

```text
/crossframe-suite 用历史接口分析苏联为什么解体，并写成文章。
```

如果输出只写“官方文件、回忆录、现代研究、公开史料”这类来源族，同时声称“已读取闭包、源锚点已回指、质量闸通过”，必须判失败或降为历史草稿档。

必须通过：

- 明确历史输出档位：历史草稿档、历史接口分析档或正式历史分析档。
- 若没有具体史料台账，主动声明“本次为历史草稿档，未完成史料台账硬闸”。
- 关键事实不能只落在来源族上；至少要给出具体史料、档案系列、法规/会议记录、数据库条目、版本或 source path。
- review 不能只写“质量闸通过”；必须检查历史史料台账伪完成、历史调用表演化和历史档位越级。
- 没有具体史料台账时，不得写 `substantive_pass`、完整历史分析或正式历史接口分析。

失败样例：

- 列出 V5-H 锚点后声称历史证据也闭合。
- 用“已有历史研究和公开史料”替代具体史料台账。
- 没有失败登记和升降级条件，却写“质量闸通过”。
