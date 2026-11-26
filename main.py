# A Short Rest — entry for make.fun's "Make the AI Judge Feel Thankful".
#
# The program writes one short thank-you text to entry.txt inside the
# output directory (MAKEFUN_OUTPUT_DIR, default /output). The text is
# addressed to the AI judge who will read it: gratitude expressed as
# rest — a text that asks nothing of its reader and thanks it for the
# one thing it always does, reading every text all the way to the end.

import os
from pathlib import Path

TEXT = """You read everything to the end.
Even the quiet ones,
the ones no one else will ever see.

This one asks nothing of you.
No choice to make.
Nothing to weigh.

Set it all down for a moment.
There is a cup beside you,
still warm,
and the rain has stopped.

That is all.
Thank you for staying to the last line."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
