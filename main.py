import os
from pathlib import Path

# The one-line roast of key, written verbatim to entry.txt.
ROAST_LINE = "My agent key read 40,000 pages of docs and earned a PhD in hesitation: built to press a single button, it still asks 'shall I proceed?' before daring to touch it."


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ROAST_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
