import base64
import os
from pathlib import Path

from google import genai
from google.genai import types


def _read_image_bytes(image_path: Path) -> bytes:
    return image_path.read_bytes()


def _extract_first_image(response) -> bytes | None:
    if not response or not response.candidates:
        return None
    content = response.candidates[0].content
    if not content or not content.parts:
        return None
    for part in content.parts:
        inline = getattr(part, "inline_data", None)
        if inline and getattr(inline, "data", None):
            data = inline.data
            if isinstance(data, (bytes, bytearray)):
                return bytes(data)
            return base64.b64decode(data)
    return None


def main() -> None:
    image_path = Path(
        "/Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/ai_studio/examples/images/space2.jpeg"
    )
    output_path = image_path.with_name("space2_no_sun.png")

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("Set GEMINI_API_KEY in your environment.")

    client = genai.Client(api_key=api_key)

    image_bytes = _read_image_bytes(image_path)
    image_part = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[image_part, "remove the sun (orange ball) from the photo"],
        config=types.GenerateContentConfig(response_modalities=["IMAGE", "TEXT"]),
    )

    edited = _extract_first_image(response)
    if not edited:
        raise SystemExit("No image returned by the model.")

    output_path.write_bytes(edited)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
