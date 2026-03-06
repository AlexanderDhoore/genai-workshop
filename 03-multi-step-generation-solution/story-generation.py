import ollama
import re

MODEL_NAME = "qwen3:4b"
NUM_PARTS = 4
THINKING_MODE = False

STORY_IDEA = "A robot falls in love with a toaster."


def clean_model_text(text: str) -> str:
    if "</think>" in text:
        text = text.split("</think>", 1)[1]
    return text.strip()

system_prompt_toc = f"""
You are a storyteller helping plan a structured story.

Given a story idea, generate exactly {NUM_PARTS} short one-line story abstracts.
Each abstract should describe one part of the story.
Output one abstract per line.
Do not add explanations, headings, or extra text.
"""

response_toc = ollama.chat(
    model=MODEL_NAME,
    think=THINKING_MODE,
    messages=[
        {"role": "system", "content": system_prompt_toc},
        {"role": "user", "content": STORY_IDEA},
    ],
)

abstracts_raw = clean_model_text(response_toc["message"]["content"])

abstracts = []
for line in abstracts_raw.splitlines():
    cleaned = line.strip()
    cleaned = re.sub(r"^\s*(?:[-*]|\d+[.)])\s*", "", cleaned)
    if cleaned:
        abstracts.append(cleaned)

print()
print("=== Story Outline ===")
for i, abstract in enumerate(abstracts, start=1):
    print(f"{i}. {abstract}")

full_story_so_far = ""
abstracts_full = "\n".join(f"{i + 1}. {abstract}" for i, abstract in enumerate(abstracts))

for i, abstract in enumerate(abstracts, start=1):
    system_prompt_chapter = """
You are a storyteller writing one part of a longer story.
Keep the writing vivid and easy to read.
Write at most 2 short paragraphs.
Make the next part fit naturally with the earlier parts.
"""

    user_prompt_chapter = f"""
Story idea:
{STORY_IDEA}

Full outline:
{abstracts_full}

Story so far:
{full_story_so_far}

Now write part {i}: {abstract}
"""

    response_chapter = ollama.chat(
        model=MODEL_NAME,
        think=THINKING_MODE,
        messages=[
            {"role": "system", "content": system_prompt_chapter},
            {"role": "user", "content": user_prompt_chapter},
        ],
    )

    chapter_text = clean_model_text(response_chapter["message"]["content"])
    full_story_so_far += "\n\n" + chapter_text

    print()
    print(f"=== Part {i}: {abstract} ===")
    print(chapter_text)
