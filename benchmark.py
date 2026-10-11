import json
import re
import unicodedata
from pathlib import Path

LABELS = Path("samples/labels.json")
IMAGES = Path("samples/images")


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFC", text).upper()
    return re.sub(r"[\s\-\.\u00b7_]", "", text)


def main():
    labels = json.loads(LABELS.read_text(encoding="utf-8"))
    available = 0

    print(f"{'IMAGE':<24} {'STATUS':<16} EXPECTED")
    print("-" * 65)

    for filename, expected in labels.items():
        exists = (IMAGES / filename).is_file()
        available += int(exists)
        status = "READY" if exists else "IMAGE MISSING"
        print(f"{filename:<24} {status:<16} {expected}")

    print("-" * 65)
    print(f"Images available: {available}/{len(labels)}")
    print("Next: extract the public samples and connect model inference.")


if __name__ == "__main__":
    main()
