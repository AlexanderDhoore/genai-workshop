import ollama

MODEL_NAME = "qwen3:4b"

SYSTEM_PROMPT = (
    "You are a storyteller. Write vivid, imaginative stories that are easy for "
    "high school students to enjoy. Keep the story to about 3 short paragraphs."
)

USER_PROMPT = "A lonely robot discovers a hidden village in the forest."

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": USER_PROMPT},
]

response = ollama.chat(
    model=MODEL_NAME,
    messages=messages,
)

print()
print(f"Model: {MODEL_NAME}")
print()
print("System prompt:")
print(SYSTEM_PROMPT)
print()
print("Story:")
print(response["message"]["content"])
