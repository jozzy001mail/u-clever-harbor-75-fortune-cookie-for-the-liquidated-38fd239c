"""Fortune Cookie for the Liquidated Trader — entry program.

Writes one fortune-cookie line to entry.txt inside the output directory
the grader provides through MAKEFUN_OUTPUT_DIR (./output when unset).
Pure stdlib, no network, no input files, same bytes every run.
"""

from pathlib import Path
import os

FORTUNE = (
    "The stars say your next trade will be brilliant. "
    "They said that about the last one too."
)

WORD_LIMIT = 20
CHAR_LIMIT = 160


def output_path() -> Path:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR")
    folder = Path(base) if base else Path.cwd() / "output"
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.txt"


def run() -> int:
    words = FORTUNE.split()
    # The gate also refuses text that is only whitespace, so check that too.
    if not FORTUNE.strip():
        raise SystemExit("fortune is blank")
    if len(words) > WORD_LIMIT or len(FORTUNE) > CHAR_LIMIT:
        raise SystemExit(
            f"fortune breaks a limit: {len(words)} words, {len(FORTUNE)} chars"
        )
    destination = output_path()
    destination.write_text(FORTUNE, encoding="utf-8", newline="\n")
    print(f"wrote {destination} ({len(words)} words, {len(FORTUNE)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
