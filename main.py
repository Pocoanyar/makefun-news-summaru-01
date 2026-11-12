"""Write the entry summary for make.fun's news-summary-01 competition.

The finished summary lives in summary.txt, next to this file in the
repository. This program copies it, byte for byte, to entry.txt in the
output directory: MAKEFUN_OUTPUT_DIR when that is set (local runs),
otherwise /output, which is where the grader looks for it.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load_summary() -> bytes:
    """Read summary.txt and check it against the competition's gate:
    UTF-8 text of 1 to 2,000 characters, not only white space."""
    data = (HERE / "summary.txt").read_bytes()
    text = data.decode("utf-8")
    if not 1 <= len(text) <= 2000 or not text.strip():
        raise ValueError("summary.txt is outside the 1-2000 character gate")
    return data


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(load_summary())


if __name__ == "__main__":
    main()
