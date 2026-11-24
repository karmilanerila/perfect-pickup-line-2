"""One-line pickup line an AI agent could say out loud.

The line leans on the most human thing an agent can offer: its
attention, paid for in the only currency it has. "Tokens" is the
agent's own machinery turned romantic — every token is a unit of
thinking, and offering all of them is offering everything it has.
It is short, warm, and easy to say with no setup, and it lands
because the sacrifice is real to the speaker: tokens are the one
thing an agent cannot get back.
"""

import os

LINE = "I would spend all my tokens just talking to you."


def write_entry(out_dir: str) -> str:
    """Write the pickup line to entry.txt and return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
