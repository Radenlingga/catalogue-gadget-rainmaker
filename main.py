"""Catalogue-gadget entry: write the Rainmaker photograph to the output path.

The photograph is entry.png beside this file: a studio catalogue shot of
the Rainmaker, a desktop gadget that holds a small rain cloud over a
single houseplant. Outside the grader's container, MAKEFUN_OUTPUT_DIR
stands in for /output.
"""

import os
import shutil
from pathlib import Path

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main() -> None:
    # A plain byte-for-byte copy, so both grader runs write identical bytes.
    source = Path(__file__).parent / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.png"
    shutil.copyfile(source, target)
    # Guard the gate: the written file must be a whole PNG within the caps.
    data = target.read_bytes()
    assert data.startswith(PNG_SIGNATURE), "entry.png is not a PNG"
    assert len(data) <= 1_048_576, "entry.png exceeds 1 MiB"


if __name__ == "__main__":
    main()
