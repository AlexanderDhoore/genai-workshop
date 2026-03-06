from pathlib import Path

import ollama

MODEL_NAME = "qwen3-vl:4b"
USER_PROMPT = "What object do you see in this image? Answer in one short paragraph."

SCRIPT_DIR = Path(__file__).resolve().parent

# TODO: Choose one of the images in the examples/ folder, or use your own image path.
IMAGE_PATH = ""

assert IMAGE_PATH.strip(), "Fill in IMAGE_PATH before running the script."

image_path = Path(IMAGE_PATH)
if not image_path.is_absolute():
    image_path = SCRIPT_DIR / image_path

assert image_path.exists(), f"Image not found: {image_path}"

response = ollama.chat(
    model=MODEL_NAME,
    messages=[
        {
            "role": "user",
            "content": USER_PROMPT,
            "images": [],  # TODO: pass the image path to the model
        }
    ],
)

print()
print(f"Model: {MODEL_NAME}")
print(f"Image: {image_path}")
print()
print("Question:")
print(USER_PROMPT)
print()
print("Answer:")
print(response["message"]["content"])
