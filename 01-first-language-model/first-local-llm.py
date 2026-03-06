import ollama

MODEL_NAME = "qwen3:4b"
SYSTEM_PROMPT = "You are a creative assistant for a high school AI workshop. Keep your answers short, playful, and easy to read."

# TODO: Write your own prompt here.
USER_PROMPT = ""

assert USER_PROMPT.strip(), "Fill in USER_PROMPT before running the script."

response = ollama.chat(
    model=MODEL_NAME,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT},
    ],
)

print()
print(f"Model: {MODEL_NAME}")
print()
print(response["message"]["content"])
