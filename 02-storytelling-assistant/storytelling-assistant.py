import ollama

MODEL_NAME = "qwen3:4b"

SYSTEM_PROMPT = (
    "You are a storyteller. Write vivid, imaginative stories that are easy for "
    "high school students to enjoy. Keep the story to about 3 short paragraphs."
)

# TODO: Enter your own creative story idea here.
USER_PROMPT = ""

assert USER_PROMPT.strip(), "Fill in USER_PROMPT before running the script."

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": ""},  # TODO: send USER_PROMPT to the model
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
