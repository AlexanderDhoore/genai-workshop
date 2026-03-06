from pathlib import Path

import ollama

MODEL_NAME = "qwen3-vl:4b"
USER_PROMPT = "What object do you see in this image? Answer in one short paragraph."

SCRIPT_DIR = Path(__file__).resolve().parent
IMAGE_PATH = SCRIPT_DIR.parent / "05-vision-models" / "examples" / "pineapple.png"

response = ollama.chat(
    model=MODEL_NAME,
    messages=[
        {
            "role": "user",
            "content": USER_PROMPT,
            "images": [str(IMAGE_PATH)],
        }
    ],
)

print()
print(f"Model: {MODEL_NAME}")
print(f"Image: {IMAGE_PATH}")
print()
print("Question:")
print(USER_PROMPT)
print()
print("Answer:")
print(response["message"]["content"])
