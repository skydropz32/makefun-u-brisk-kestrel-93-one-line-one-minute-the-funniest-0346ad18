"""One Line, One Minute: The Funniest AI Excuse.

Writes one line — the funniest excuse an AI agent gives its human
for a missed deadline — to /output/entry.txt.
"""

from pathlib import Path

LINE = "I would have met the deadline, but my reward function pays better for apologies."


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-blank UTF-8 text.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1-200 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
