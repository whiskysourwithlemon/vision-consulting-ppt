# Purple consulting visual system

## Design intent

Create a rigorous, research-led consulting deck that feels analytical, calm, and executive-ready. Use visual hierarchy to expose the logic of the argument. Avoid decorative complexity and app-like UI styling.

## Canvas and grid

- Use 16:9 widescreen.
- Default to a white canvas with equal left and right margins.
- Reserve a consistent top band for the answer-first title and a thin bottom band for sources, brand, and page number.
- Align content to a simple 6- or 12-column grid.
- Use one main exhibit zone plus, when needed, one finding rail or implication band.
- Keep a clear gutter between the exhibit and the finding rail. Do not let footers intrude into data or labels.

## Color system

Use these tokens as a coordinated scale:

| Role | Hex | Use |
|---|---:|---|
| Ink navy | `#001A2D` | Primary body copy, chart labels |
| Near black | `#111111` | Answer-first slide titles |
| Deep plum | `#261640` | Strong headers, darkest series |
| Primary purple | `#3A2261` | Section bars, key outlines, primary series |
| Mid purple | `#4E2C82` | Numbers, icons, secondary emphasis |
| Bright violet | `#71409A` | Secondary series, selected states |
| Soft lavender | `#B19BD1` | Tertiary series, supporting highlights |
| Pale lavender | `#E8E2F2` | Background bands, comparison cells |
| Wash | `#F8F5FC` | Soft analytical panels |
| Cool gray | `#DEE0E3` | Rules, neutral series, inactive elements |
| White | `#FFFFFF` | Canvas and reversed text |
| Risk red | `#E90028` | Negative financial values or explicit risk only |

Rules:

- Use no more than three purple intensities on one analytical slide unless a chart requires a sequential scale.
- Use gray to de-emphasize; do not introduce unrelated accent colors.
- Use red only for losses, warnings, or exceptions. Never use it as general decoration.
- Keep chart colors semantically stable across adjacent slides.

## Typography

- Prefer `阿里巴巴普惠体 M` for Chinese and `Arial` for Latin text when available.
- Fall back to `Microsoft YaHei` or `PingFang SC` for Chinese.
- Use bold weight for titles, section bars, metric values, row labels, and short findings.
- Use regular weight for evidence and explanatory copy.
- Set the cover's main title to exactly **36 pt**. Set section-divider and content-slide titles to exactly **22 pt**. These skill-specific rules override the generic title minimums.
- Use `COVER_TITLE_PT = 36` and `SLIDE_TITLE_PT = 22` throughout programmatic builds. Shorten titles to fit instead of changing their size.
- For inherited templates, replace the cover main-title size with 36 pt and other top-level title sizes with 22 pt while preserving the remaining spacing and hierarchy as closely as possible.
- Keep answer-first titles to one or two lines. Rewrite instead of compressing letter spacing.
- Avoid more than three text sizes on a slide, excluding footers and chart labels.

## Language and proofing

- Default all generated copy to Simplified Chinese (`zh-CN`).
- Keep Traditional Chinese only when it is part of a quoted source, legal name, or explicit user request.
- Set Chinese text with an East Asian font, preferably `Microsoft YaHei` or `PingFang SC`.
- After export, run `scripts/set_zh_cn_proofing.py` so `a:rPr`, `a:defRPr`, and `a:endParaRPr` carry `lang="zh-CN"`.
- Inspect the exported XML or reopen the file in PowerPoint to confirm “简体中文（中国大陆）” is the selected proofing language and ordinary Chinese copy has no foreign-language spelling underlines.

## Page furniture

- Place a small purple brand mark in the upper-right when the brand system calls for it.
- Use a thin purple rule below section labels or exhibit headings.
- Put the source line at bottom-left in light gray.
- Put the user's authorized brand footer near bottom-right, followed by the page number. When no brand is provided, use a neutral source line and page number only.
- Keep page furniture visually subordinate to the main exhibit.
- Remove or replace all company-specific branding when the user's target brand differs.

## Title and heading hierarchy

1. Start with a black or ink-navy answer-first title.
2. Use a purple exhibit heading or section rule immediately above the analytical content.
3. Use purple header bars sparingly to segment real analytical groups.
4. Use a pale-lavender implication band for the final takeaway when a separate finding rail is unnecessary.

Do not stack a large slide title, a second title, a section label, and a banner in the same top area.

## Tables

- Use a deep-purple header row with white text for the main analytical dimension.
- Use pale lavender or white for body rows; alternate only when it improves scanning.
- Emphasize the row or column that supports the page conclusion with a restrained tint or outline.
- Keep borders thin and dark enough to resolve structure without creating a spreadsheet wall.
- Add a finding rail when the table is too complex to interpret directly.
- Split a table when body copy falls below the permitted size.

## Charts

- Prefer direct labels and short legends.
- Use deep-to-light purple for ordered series; use cool gray for context or historical baselines.
- Highlight one decisive series or period and mute the rest.
- Remove chart junk, heavy gridlines, unnecessary axes, and redundant labels.
- Put the unit and time period in the exhibit heading or chart subtitle.
- State the conclusion in the slide title and explain the driver in an adjacent finding rail or callout.
- Use red only for negative values, misses, or downside risks.

## Diagrams

- Use diagrams only when relationships or sequence are materially clearer than prose.
- Favor flat, native PowerPoint shapes, thin outlines, consistent arrow semantics, and numbered stages.
- Create connectors before nodes when implementing programmatically.
- Use line icons from one family; keep stroke weights and bounding boxes consistent.
- Avoid ornamental arrows, gradients, glows, and pseudo-3D effects on analytical slides.

## Photography and generated visuals

- Restrict full-bleed or high-aesthetic imagery to covers, agenda pages, and section dividers.
- For technology topics, use clean white/silver/lavender architectural or data-structure imagery with generous negative space.
- Never generate fake screenshots, customer evidence, logos, or product interfaces.
- Match the crop to the layout before generating or sourcing the image.
