---
name: vision-consulting-ppt
description: Transform text-heavy, blank-layout, or roughly formatted PPT/PPTX drafts into editable purple consulting-style presentations with conclusion-led titles, rigorous analytical logic, structured exhibits, charts, tables, executive findings, and optional semantically matched outline icons. Use for Chinese or bilingual commercial due diligence, investment committee, strategy, market research, technology analysis, company analysis, financial forecast, and valuation decks; trigger when users ask for 紫色咨询风格、专业咨询公司风格、把纯文字PPT改成专业咨询PPT, or to add restrained semantic icons beside modules or stages.
---

# Purple Consulting PPT

Turn raw research and text-first slides into decision-oriented consulting exhibits. Preserve facts and meaning while rebuilding information hierarchy, narrative flow, and slide composition.

## Apply the mandatory defaults

- Write all generated presentation copy in Simplified Chinese by default, including titles, body text, chart labels, table text, findings, source lines, and speaker notes. Keep English only for proper nouns, abbreviations, formulas, or when the user explicitly requests bilingual or another language.
- Set the cover's main title to exactly **36 pt**. Set section-divider titles and answer-first content-slide titles to exactly **22 pt**. These are intentional overrides of the `presentations` skill's generic title minimums. Do not silently enlarge or shrink either class; shorten or rewrite copy to fit.
- Use exactly two shared title constants in programmatic builds: `COVER_TITLE_PT = 36` and `SLIDE_TITLE_PT = 22`. Do not create page-specific title sizes.
- Use a Simplified Chinese font for all Chinese text. Prefer `Microsoft YaHei`; fall back to `PingFang SC` when required by the user's environment.
- After exporting the PPTX, run `scripts/set_zh_cn_proofing.py` on the final deck. This writes `zh-CN` into DrawingML text properties so PowerPoint defaults to “简体中文（中国大陆）” instead of treating Chinese copy as a foreign-language spelling error.

## Load the required guidance

1. Read and follow the installed `presentations` skill before inspecting or producing any PPTX. Treat its hard requirements as binding.
2. Read [references/style-system.md](references/style-system.md) before planning typography, color, charts, tables, or page furniture.
3. Read [references/transformation-workflow.md](references/transformation-workflow.md) when the input is a text-heavy deck, outline, report, spreadsheet, or collection of research materials.
4. Read [references/layout-catalog.md](references/layout-catalog.md) before mapping content to layouts. Treat its patterns as abstract layout guidance and never reuse source-project copy, screenshots, names, portraits, or data.
5. When the user provides a licensed template or mature reference deck, follow the `presentations` skill's template workflow. This public skill intentionally bundles no branded templates or proprietary reference decks.
6. Read [references/icon-system.md](references/icon-system.md) whenever icons could improve stage scanning, model comparisons, process steps, capability layers, callouts, or section lead-ins. Use only user-provided, self-created, public-domain, or permissively licensed icons.

## Choose the authoring route

Classify the input before editing:

- **Content-only or blank-layout draft:** Treat the deck as a content source, not a visual template. Extract all claims, evidence, tables, charts, notes, and sources; then create a new deck under the explicit custom visual direction defined by this skill.
- **Formal branded template or mature reference deck:** Follow the `presentations` skill's template-following workflow. Duplicate suitable source slides and edit inherited elements in place.
- **Mixed deck:** Preserve genuinely mature slides and rebuild unfinished text-only slides. Keep one visual system and document every intentional deviation.
- **No source deck:** Build from the user's outline, report, or data. Define the narrative and slide plan before drawing.

Never paste a redesigned layer over a blank source slide merely to retain its page count. Rebuild the content in a clean deck unless template inheritance is genuinely required.

## Execute the consulting workflow

1. **Define the decision job.** State the audience, decision, central takeaway, and evidence needed.
2. **Audit the source completely.** Render and inspect every slide. Inventory claims, data, source footers, charts, tables, images, unresolved notes, and duplicated content.
3. **Build the storyline.** Use a cumulative arc such as context → evidence → implication → recommendation. Make section dividers signal a change in question, not just a topic label.
4. **Rewrite each page.** Give every slide one answer-first title, one analytical job, one primary exhibit, and one implication. Preserve all factual qualifications.
5. **Select a layout.** Match the content to the smallest suitable pattern in the layout catalog. Split dense material before shrinking type.
6. **Draw the exhibit.** Use native editable text, shapes, charts, and tables where appropriate. Use real images or generated abstract visuals only when they materially improve understanding.
7. **Add icons selectively.** Choose icons by meaning from an approved source, inspect candidates, recolor working copies to ink navy or purple, and place them beside the relevant stage or heading. Omit icons when they do not improve comprehension.
8. **Apply the style system.** Maintain the purple hierarchy, white canvas, disciplined rules, consistent numbering, source line, optional user-brand zone, and page number.
9. **Add provenance.** Put `[Sources]` blocks in speaker notes for external claims and assets. Retain source footers from the input when they remain valid. Record the creator, URL, and license for every externally sourced visual asset.
10. **Apply Chinese proofing metadata.** Run `python3 scripts/set_zh_cn_proofing.py <final.pptx>` after export and before final rendering. Re-run it after every rebuilt export.
11. **Render and inspect.** Review every slide at full size. Fix wrapping, overlap, clipping, tiny copy, weak alignment, inconsistent symbols or icon sizes, chart errors, unresolved placeholders, accidental Traditional Chinese, and missing `zh-CN` text metadata.

## Enforce the content grammar

- Write titles as defensible conclusions, not labels such as “市场规模” or “技术路线”.
- Convert long prose into claim → evidence → implication, not decorative cards.
- Convert raw lists into mutually exclusive groups, stages, comparison dimensions, or decision criteria only when the source supports that structure.
- Convert numeric evidence into a chart only when the visual comparison is clearer than a table.
- Put the decisive interpretation beside or below the exhibit; never make the audience infer the point unaided.
- Keep a visible distinction between fact, management statement, estimate, assumption, and consultant judgment.
- Do not invent metrics, sources, customers, quotes, causal claims, or forecast assumptions.
- Use a continuation marker such as `(1/3)` only for a real multi-page analytical sequence.

## Preserve quality over density

- Keep the cover's main title at exactly 36 pt and every section-divider or content-slide title at exactly 22 pt. For other text, honor the `presentations` skill's minimum font sizes unless the user provides a different standard.
- Shorten, restructure, or split before reducing font size.
- Prefer one dominant composition. Avoid dashboard-like card grids unless the content is inherently modular.
- Use accent purple to encode hierarchy, not to decorate every object.
- Use icons as semantic anchors beside stages, headings, or model roles. Keep them monochrome, consistently sized, and limited to one per semantic unit; never scatter them decoratively.
- Keep decorative imagery mostly on covers, agendas, and dividers; evidence pages should remain analytical.
- Avoid the source project's observed failure modes: oversized titles colliding with section labels, dense tables without a reading path, stacked sidebars covering content, and footers competing with the exhibit.

## Keep the public skill clean

- Never add source-deck screenshots, customer materials, management portraits, company-confidential data, local computer paths, comments, speaker notes, or document author metadata to this skill.
- Never bundle company logos, branded templates, proprietary icon libraries, paid fonts, or third-party assets unless redistribution rights are explicit.
- Keep user-provided confidential content inside the user's working output only; do not persist it into this reusable skill folder.
- Before publishing an update, scan text and presentation metadata and inspect every image asset at full size.

## Deliver

Return an editable PPTX, not flattened slide images. Preserve the original input and export a new file unless the user explicitly requests an in-place edit. Confirm that the cover title is 36 pt, section-divider and content-slide titles are 22 pt, and the text proofing language is `zh-CN`. Briefly summarize the narrative and visual changes, and cite the final deck exactly once using the `presentations` skill's required output citation.
