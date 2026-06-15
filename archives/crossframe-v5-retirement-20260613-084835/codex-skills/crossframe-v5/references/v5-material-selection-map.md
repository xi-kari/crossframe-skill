# v5 Material Selection Map

本文件是 v5 的材料选择中间层。它把一次请求先映射到 v5 单一源文本中的 source module，再由 source module 推出连读包、专项 skill 和 capsule 摘要边界。

使用规则：

- 先选 `source_module_id`，再选 `v5-continuity-bundles.md` 中的连读包条目。
- 本文件只保存模块级路由，不复制 v5 原文。
- 每次普通任务只读取命中的 source module 条目；不得整块加载本文件、`v5-source-spine.md`、`v5-section-digest-index.md` 或完整连读包。
- 若 source module 未命中但概念卡被触发，先回到本文件补 source module；补不上则降档。

| source_module_id | 源范围 | 触发话题 | 必读相邻模块 | 对应连读包 | 可触发专项 skill | 降档规则 | capsule 摘要预算 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sm-use-boundary-entry | P0405-P0476; P0477-P0575; P0755-P0787 | 任何诊断、框架使用、低权力主体、准入、降级、退出、概念误用 | sm-seven-gates-mainline; sm-core-concept-layers | v5-use-boundary-low-power-pack | crossframe-v5; crossframe-v5-review | 未处理准入、退出和低权力保护时，不得进入强判断或行动建议。 | 120-220 字 |
| sm-seven-gates-mainline | P0717-P0754; P1505-P1591; P1599-P1724 | 实质诊断、组织/公共判断、深度分析、机制候选、L1-L3 输出 | sm-use-boundary-entry; 证据经由 AI、平台、表格或流程中介时追加 sm-evidence-ai-process | v5-seven-gates-diagnosis-pack | crossframe-v5; crossframe-v5-review | G1-G7 未过时，只能输出观察、问题清单或补证条件。 | 160-260 字 |
| sm-observation-reflexivity | P0555-P0573; P1264-P1268; P1523-P1527; P2168-P2186 | 观察、命名、评分、公开、发布后反应、对象被诊断改变 | sm-seven-gates-mainline; sm-judgment-responsibility when public | v5-observation-reflexivity-pack | crossframe-v5-public; crossframe-v5-review | 未区分基线/响应/发布后反应时，不得把反应写成本质。 | 120-220 字 |
| sm-judgment-responsibility | P0445-P0458; P0742-P0754; P1214-P1216; P1592-P1598; P1777-P1794; P2328-P2343; P2366-P2376 | 方向性判断、公开判断、处分、名誉、资源、资格、权利、开放断言 | sm-seven-gates-mainline; sm-evidence-ai-process | v5-judgment-responsibility-pack | crossframe-v5-debate; crossframe-v5-public; crossframe-v5-review | 八件套或撤回条件缺失时，不得发布强判断。 | 160-280 字 |
| sm-evidence-ai-process | P0529-P0555; P0690-P0704; P1641-P1661; P2151-P2167; P2187-P2227 | AI 报告、合规材料、表格流程、平台指标、弱信号、缺席材料、不透明 | sm-seven-gates-mainline; 涉及平台或机构时追加 sm-public-institution | v5-evidence-ai-process-pack | crossframe-v5-public; crossframe-v5-review | 只有过程材料或 AI 文本时，降为线索、问题清单或开放断言。 | 160-260 字 |
| sm-core-concept-layers | P0788-P0833; P0834-P0890; P0891-P1009; P1010-P1109; P1110-P1206; P2135-P2150 | 锚点、承接/回流、边界、势场、结构负荷、过程组、概念上升、哲学随笔 | sm-use-boundary-entry; sm-seven-gates-mainline | v5-core-concept-integrity-pack | crossframe-v5-essay; crossframe-v5-teach; crossframe-v5-review | 概念承担判断作用但未回到相邻模块时，只能做表达解释，不得做因果判断。 | 180-320 字 |
| sm-root-assumptions | P1207-P1307 | 根假设、元约束、核心推论、非闭合行动、文明尺度基础 | sm-lifecycle-governance-dynamics; sm-use-boundary-entry | v5-root-evolution-deep-pack | crossframe-v5-notebook; crossframe-v5-essay | 未给反向条件时，不得写全称规律或文明命运。 | 120-220 字 |
| sm-lifecycle-governance-dynamics | P1308-P1392; P1393-P1504; P1721-P1724 | 长期演化、阶段判断、递进、势场、自主解离、多中心治理、未来探索者、三年/五年推演 | sm-root-assumptions; 使用报告或指标推演时追加 sm-evidence-ai-process | v5-root-evolution-deep-pack | crossframe-v5-notebook; crossframe-v5-essay; crossframe-v5-review | 必要变量和反向信号不足时，不得排序主路径或给趋势结论。 | 180-320 字 |
| sm-action-hard-rules | P0733-P0741; P1725-P1815 | 行动建议、低条件试探、主动收束、诊断/干预分离、责任链硬规则 | sm-seven-gates-mainline; sm-judgment-responsibility | v5-action-healing-transfer-pack | crossframe-v5-org; crossframe-v5-public; crossframe-v5-review | 权力封闭或行动上限不明时，不得给正式干预方案。 | 140-240 字 |
| sm-healing-transfer-t0-t4 | P1867-P1951 | 疗愈、撤离、转移、演化记忆保存、安全环境、信任载体 | sm-love-trapped-trauma; sm-action-hard-rules | v5-action-healing-transfer-pack | crossframe-v5-dialogue; crossframe-v5-org; crossframe-v5-review | T0 安全条件不成立时，不得推进 T1-T4 操作。 | 140-260 字 |
| sm-love-trapped-trauma | P0604-P0689; P1296-P1305; P1816-P1861; P2228-P2275 | 爱、牺牲、照护、亲密伤害、无法退出、复杂创伤、无健康基准、不浪费爱 | sm-use-boundary-entry; sm-healing-transfer-t0-t4 | v5-love-trapped-trauma-pack; v5-action-healing-transfer-pack | crossframe-v5-dialogue; crossframe-v5-essay; crossframe-v5-review | 未保护无法退出主体时，不得把爱写成忍耐或修复命令。 | 180-320 字 |
| sm-public-institution | P0717-P0754; P1952-P2037; P2038-P2075 | 公共议题、组织权力、平台治理、通道控制、解释锚、公共承诺、生产/分配/再生产 | sm-evidence-ai-process; 涉及公开判断时追加 sm-judgment-responsibility | v5-public-power-institution-pack | crossframe-v5-public; crossframe-v5-org; crossframe-v5-review | 申诉、反报复、外部复核不成立时，降为风险假设或复核请求。 | 180-320 字 |
| sm-domain-translation | P0574-P0590; P1805-P1807; P1990-P2010; P2018-P2037; P2276-P2297 | 阶级、资本、国家、意识形态、社会主义、共产主义、官场、职场、物理隐喻、经典来源 | sm-core-concept-layers; sm-public-institution when institutional | v5-domain-translation-pack | crossframe-v5-notebook; crossframe-v5-essay; crossframe-v5-review | 未翻译成结构变量时，不得用领域词直接证明结论。 | 140-260 字 |
| sm-framework-governance | P0575-P0590; P2076-P2146; P2298-P2365; P2368-P2376 | 修改框架、设计 skill、工具化、商业化、课程化、AI 工具、版本治理、框架退场 | sm-use-boundary-entry; sm-evidence-ai-process | v5-framework-governance-pack | crossframe-v5-casebook; crossframe-v5-review | 不得用框架自证框架安全；必须保留外部评审或退场接口。 | 180-320 字 |

## 常用组合

| 场景 | source modules | 不应自动加入 |
| --- | --- | --- |
| 弱者如何寻安宁、脆弱与承接、哲学随笔 | sm-use-boundary-entry; sm-seven-gates-mainline; sm-core-concept-layers | sm-evidence-ai-process; sm-public-institution; sm-framework-governance |
| AI 合规报告能否证明平台申诉有效 | sm-use-boundary-entry; sm-seven-gates-mainline; sm-evidence-ai-process; sm-public-institution | 除非出现伤害或无法退出，否则不自动加入 sm-love-trapped-trauma |
| 未来探索者推演三年后走向 | sm-use-boundary-entry; sm-seven-gates-mainline; sm-root-assumptions; sm-lifecycle-governance-dynamics | 除非出现强领域词，否则不自动加入 sm-domain-translation |
| 亲密伤害、照护、无法退出 | sm-use-boundary-entry; sm-love-trapped-trauma; sm-healing-transfer-t0-t4 | 除非组织/制度权力介入，否则不自动加入 sm-public-institution |
| 公开强判断或资源资格影响 | sm-use-boundary-entry; sm-seven-gates-mainline; sm-judgment-responsibility; sm-evidence-ai-process | 除非出现长期演化判断，否则不自动加入 sm-root-assumptions |
