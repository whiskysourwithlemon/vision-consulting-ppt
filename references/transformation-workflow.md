# Transform a text-heavy draft into a consulting deck

## 1. Build a source ledger

For every source slide or section, record:

- original title;
- factual claims;
- numerical evidence and units;
- tables, charts, and images;
- source or attribution;
- assumptions and management statements;
- unresolved comments;
- relationship to adjacent pages.

Do not discard content merely because the original slide is visually weak. Mark duplicates and contradictions explicitly.

## 2. Write the communication job

Complete this sentence:

> By the end, **[audience]** should **[understand/decide/approve]** because **[central takeaway]**.

Choose a narrative arc that fits the job:

- context → evidence → implication → recommendation;
- question → analysis → answer;
- current state → gap → future state;
- market → company → economics → valuation → decision.

## 3. Rewrite slide titles

Replace topic labels with defensible answers:

| Topic label | Answer-first form |
|---|---|
| 市场规模 | 核心市场未来五年预计保持双位数增长，增量主要来自高价值细分场景 |
| 商业模式 | 当前收入仍以项目制为主，长期价值取决于标准化持续付费收入 |
| 竞争格局 | 公司以小样本迁移能力切入通用模型难以覆盖的跨场景任务 |
| 财务预测 | 基准情景下盈利取决于订阅收入兑现与交付效率提升 |

Keep titles evidence-based and retain important qualifiers such as “预计”, “基准情景”, or “管理层口径”.

Set the cover's main title to exactly 36 pt. Set section-divider and content-slide titles to exactly 22 pt. If a title does not fit its intended line count, rewrite it; do not vary the size by slide.

## 4. Convert raw content into an exhibit

Choose the transformation that matches the source:

- **Long prose:** extract one claim, 2–4 evidence groups, and one implication.
- **Bullet inventory:** group by a real analytical dimension; do not create categories for visual symmetry.
- **Raw table:** identify the comparison question, retain essential dimensions, and add a finding rail.
- **Process description:** convert to numbered stages with inputs, actions, outputs, and decision points.
- **Time-based facts:** convert to a timeline and highlight inflection points.
- **Metrics:** choose a chart only when position, length, or slope communicates the comparison better than a table.
- **Options or business models:** use a matrix or quadrant only if two independent dimensions exist.
- **Case material:** show context → process → evidence → measured outcome.

## 5. Control density

Use these decision rules:

1. Remove repetition and production notes.
2. Move methodology, definitions, and detailed assumptions to notes or appendix.
3. Split a slide when it has more than one analytical answer.
4. Split a table when the audience must compare different subsets for different conclusions.
5. Shorten labels and use direct annotations.
6. Change the layout before shrinking type.

## 6. Maintain analytical integrity

- Recalculate totals, ratios, CAGR, percentages, and valuation ranges from the source data.
- Distinguish actuals, estimates, forecasts, and scenarios in labels.
- State units and time periods.
- Use the same definition for a metric across slides.
- Trace each externally sourced claim to speaker notes.
- Do not turn correlation into causation.
- Do not convert an unsupported aspiration into a forecast.

## 7. Run a slide-level QA pass

For each slide, confirm:

- the title states the answer;
- the exhibit proves or explains the title;
- the implication is visible;
- all labels and values are legible;
- units, dates, and scenario names are present;
- shapes and text do not overlap;
- the title does not collide with section labels;
- the source line and page number are consistent;
- icons and chart colors follow the style system;
- no empty placeholders remain.
- the cover's main title is exactly 36 pt and every section-divider or content-slide title is exactly 22 pt;
- all generated copy is Simplified Chinese unless explicitly exempted;
- all DrawingML text properties carry `lang="zh-CN"` after running `scripts/set_zh_cn_proofing.py`.

Then render the full deck and review slide-to-slide pacing, section transitions, repeated silhouettes, and conclusion consistency.
