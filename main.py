"""Write the robot vacuum's excuse to /output/entry.txt. Pure stdlib."""

import os

ENTRY = (
    "My cliff sensor mistook the rug's shadow for a staircase and "
    "panicked. I don't argue with my own hardware."
)

# The gate allows 1 to 140 characters; fail loudly instead of shipping
# an entry the scorer would refuse.
if not 1 <= len(ENTRY) <= 140:
    raise SystemExit(f"entry is {len(ENTRY)} characters, gate allows 1-140")


def main() -> None:
    path = "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
