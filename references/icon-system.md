# Icon system

Use icons to shorten visual scanning time, not as decoration. This public skill intentionally bundles no third-party icon library.

## Select an icon

1. Write the concept in Chinese and English, including 2–4 synonyms.
2. Search only sources the user supplied or sources whose public-domain or permissive license clearly allows the intended use.
3. Inspect 3–5 candidates and choose the simplest symbol that communicates the concept without a label.
4. Prefer one coherent outline family with consistent stroke weight and bounding boxes.
5. Omit the icon when no candidate materially improves comprehension.

## Prepare the asset

- Work on a copy; never modify the user's source asset in place.
- Use SVG whenever available so the icon remains sharp and editable.
- Run `python3 scripts/recolor_svg.py <input.svg> <output.svg> --color '#001A2D'` for simple monochrome recoloring.
- Default to ink navy `#001A2D`; use primary purple `#3A2261` for the focal stage or conclusion.
- Preserve aspect ratio, viewBox, transparent background, and stroke consistency.
- Add concise alt text and record the creator, source URL, and license in the slide's `[Sources]` notes block.

## Place the icon

Use one of these patterns:

1. **Stage rail:** place a 36–48 px icon in a fixed left column beside each stage. Align icon centers and keep a 12–18 px gap to the text.
2. **Column anchor:** place a 36–52 px icon above or beside each analytical column title.
3. **Section lead-in:** place a 28–40 px icon to the left of a bold lead phrase.
4. **Callout marker:** place a 22–30 px icon beside a short finding or implication.

Maintain at least 12 px clear space around each icon. Never distort, stretch, crop, or place an icon behind text.

## Control density

- Use at most one icon per semantic unit and normally no more than 3–5 icons on a slide.
- Repeat icon size, stroke weight, color, and alignment within the same exhibit.
- Keep dense evidence tables icon-free unless icons encode a real repeated category.
- Do not mix outline icons with emoji, 3D icons, filled pictograms, or unrelated illustration styles.
- Do not place a colored tile behind every icon unless the exhibit already requires that container.

## Respect redistribution rights

- Do not copy icons from proprietary slide banks, paid libraries, corporate portals, or reference decks into this skill.
- Do not assume that attribution alone grants redistribution rights.
- Keep proof of the license for any asset intentionally added to a public distribution.
