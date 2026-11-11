# Cutest cat entry for make.fun (cutest-cat-01).
#
# The entry is the cat picture held in this repository (entry.png).
# This program copies it, byte for byte, to the output directory
# as entry.png. It is deterministic: the same input bytes always
# produce the same output bytes. Standard library only.

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Confirm the copy is complete: same size as the source, so a
    # truncated write can never pass silently.
    if os.path.getsize(dst) != os.path.getsize(src):
        print("entry.png copy is incomplete", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
