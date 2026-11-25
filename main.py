import os
from pathlib import Path

LINE = "My agent key read 40,000 pages of documentation and became the world's most informed coward: it still asks 'shall I proceed?' before pressing the button it was built to press."


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
