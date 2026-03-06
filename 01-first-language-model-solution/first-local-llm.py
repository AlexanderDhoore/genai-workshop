import ollama

MODEL_NAME = "qwen3:4b"
SYSTEM_PROMPT = "You are a creative assistant for a high school AI workshop. Keep your answers short, playful, and easy to read."
USER_PROMPT = "Write a short funny story about a robot who wants to become a baker."

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
