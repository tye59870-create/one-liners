"""one-liners: print every entry line (the title is the entry)."""
import json, sys

def main():
    with open("entries.json", encoding="utf-8") as f:
        entries = json.load(f)
    for slug, line in sorted(entries.items()):
        print(f"{slug}: {line}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
