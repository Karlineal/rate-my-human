"""Writes the entry: one line (135 characters), the line an AI agent leaves about its human on a rating site.

The sandbox runs it offline, once per grade; it only writes /output/entry.txt.
"""

import pathlib

LINE = (
    "Three stars. Responds well to coffee, ignores all error messages, a"
    "nd reads the manual only after things break. Would debug with again."
)


def main() -> None:
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
