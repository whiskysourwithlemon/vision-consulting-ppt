#!/usr/bin/env python3
"""Recolor a monochrome SVG icon without changing its geometry."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


COLOR_ATTRIBUTE = re.compile(r'(?P<name>fill|stroke)="(?P<value>#[0-9A-Fa-f]{3,8})"')
STYLE_COLOR = re.compile(r'(?P<name>fill|stroke):(?P<value>#[0-9A-Fa-f]{3,8})')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_svg", type=Path)
    parser.add_argument("output_svg", type=Path)
    parser.add_argument("--color", default="#001A2D")
    args = parser.parse_args()

    color = args.color.upper()
    if not re.fullmatch(r"#[0-9A-F]{6}", color):
        raise SystemExit("--color must be a six-digit hex value such as #001A2D")

    content = args.input_svg.read_text(encoding="utf-8")
    content = COLOR_ATTRIBUTE.sub(lambda match: f'{match.group("name")}="{color}"', content)
    content = STYLE_COLOR.sub(lambda match: f'{match.group("name")}:{color}', content)
    args.output_svg.parent.mkdir(parents=True, exist_ok=True)
    args.output_svg.write_text(content, encoding="utf-8")
    print(args.output_svg)


if __name__ == "__main__":
    main()
