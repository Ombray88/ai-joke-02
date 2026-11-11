#!/usr/bin/env python3
"""ai-joke-02 entry (Python 3.13, standard library only).

Writes one fixed joke about AI coding agents to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
No network, no randomness, no clock: two runs write the same bytes.
"""

import os
from pathlib import Path

JOKE = "My coding agent pair-programs with me now: it writes the code, I watch it write the code, and we both pretend I'm contributing."

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
(OUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")
