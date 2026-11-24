"""Real-Life Patch Notes: The Comedy Changelog.

Writes one line -- a software patch note for a bug in real life /
human biology -- to /output/entry.txt.
"""

import os

ENTRY = (
    "v3.7.2: fixed a memory leak where the brain keeps every "
    "embarrassing thing you said in 2011 but forgets why you opened the fridge."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
