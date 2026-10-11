import argparse
import json
from pathlib import Path

from PIL import Image

OUTPUT_DIR = Path("/app/output")


def predict(image: Image.Image) -> tuple[str, float]:
    """Replace with the selected pretrained OCR model."""
    raise NotImplementedError("OCR model has not been integrated yet.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-image", required=True)
    args = parser.parse_args()

    input_path = Path(args.input_image)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with Image.open(input_path) as source:
        image = source.convert("RGB")

    text, confidence = predict(image)

    result = {
        "text": str(text),
        "confidence": max(0.0, min(1.0, float(confidence)))
    }

    output_path = OUTPUT_DIR / f"{input_path.stem}_output.json"
    output_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
