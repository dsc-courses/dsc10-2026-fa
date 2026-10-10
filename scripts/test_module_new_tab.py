#!/usr/bin/env python3
"""Regression check: in-scope schedule links in module.html open in a new tab."""

from pathlib import Path

MODULE_LAYOUT = Path(__file__).resolve().parent.parent / "_layouts" / "module.html"

# Each pattern must appear in the layout (substring match).
REQUIRED = [
    ("non-lecture title", '<a href="{{ event.url }}" target="_blank">{{ event.title }}</a>'),
    ("lecture code (event.url)", '<a href="{{ event.url }}" target="_blank">'),
    ("lecture code (event.code)", '<a href="{{ event.code }}" target="_blank">'),
    ("write button", '<a href="{{ event.html }}" target="_blank">'),
    ("reading link", '<a href="{{ reading.url }}" target="_blank">'),
]


def main() -> int:
    text = MODULE_LAYOUT.read_text(encoding="utf-8")
    errors = []
    for name, pattern in REQUIRED:
        if pattern not in text:
            errors.append(f'missing target="_blank" for {name}: expected {pattern!r}')
    if errors:
        for err in errors:
            print(f"FAIL: {err}")
        return 1
    print('OK: all in-scope module links have target="_blank"')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
