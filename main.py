"""Write the weirdest job title to the entry file.

Stdlib only. Reads MAKEFUN_OUTPUT_DIR when set, otherwise /output/entry.txt.
"""
import os


TITLE = "Professional Apologizer for Other People's Dogs"


def main() -> None:
    if not (1 <= len(TITLE) <= 60) or not TITLE.strip():
        raise SystemExit("title must be 1-60 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
