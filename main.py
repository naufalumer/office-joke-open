import os

ENTRY = "I replied-all to the reply-all warning, and now HR, IT, and the printer are all in a meeting about me."


def main():
    # Write the joke exactly, with no trailing newline, per the rules.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
