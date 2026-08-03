#!/usr/bin/env python3
"""Set PowerPoint DrawingML proofing language to Simplified Chinese."""

from __future__ import annotations

import argparse
import os
import re
import tempfile
import zipfile
from pathlib import Path


TEXT_PROPERTY_TAG = re.compile(
    rb"<a:(?:rPr|defRPr|endParaRPr)\b[^>]*>",
)
LANGUAGE_ATTRIBUTE = re.compile(
    rb"\s+(?:lang|altLang)=(?:\"[^\"]*\"|'[^']*')",
)


def set_zh_cn(tag: bytes) -> bytes:
    """Replace existing proofing metadata and add lang=zh-CN."""
    cleaned = LANGUAGE_ATTRIBUTE.sub(b"", tag)
    if cleaned.endswith(b"/>"):
        return cleaned[:-2] + b' lang="zh-CN"/>'
    return cleaned[:-1] + b' lang="zh-CN">'


def patch_xml(data: bytes) -> tuple[bytes, int]:
    patched, count = TEXT_PROPERTY_TAG.subn(
        lambda match: set_zh_cn(match.group(0)),
        data,
    )
    return patched, count


def rewrite_pptx(source: Path, target: Path) -> int:
    """Rewrite PPTX XML while preserving the remaining package entries."""
    target.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        prefix=f".{target.stem}.",
        suffix=".pptx",
        dir=target.parent,
        delete=False,
    )
    temporary = Path(handle.name)
    handle.close()
    total = 0

    try:
        with zipfile.ZipFile(source, "r") as input_zip:
            with zipfile.ZipFile(temporary, "w") as output_zip:
                for item in input_zip.infolist():
                    data = input_zip.read(item.filename)
                    if item.filename.startswith("ppt/") and item.filename.endswith(".xml"):
                        data, count = patch_xml(data)
                        total += count
                    output_zip.writestr(item, data)
        os.replace(temporary, target)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise

    return total


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Set a:rPr, a:defRPr, and a:endParaRPr language metadata "
            "to zh-CN in a PPTX package."
        ),
    )
    parser.add_argument("pptx", type=Path, help="Input PPTX; edited in place by default.")
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional output PPTX path. Omit to edit the input file in place.",
    )
    args = parser.parse_args()

    source = args.pptx.expanduser().resolve()
    target = args.output.expanduser().resolve() if args.output else source
    if not source.is_file():
        parser.error(f"Input file does not exist: {source}")
    if source.suffix.lower() != ".pptx":
        parser.error("Input must be a .pptx file.")

    count = rewrite_pptx(source, target)
    print(f"Updated {count} DrawingML text-property tags to zh-CN: {target}")


if __name__ == "__main__":
    main()
