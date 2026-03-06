import gradio as gr
import ollama

MODEL_NAME = "qwen3:4b"
SYSTEM_PROMPT = """
You are an interactive storytelling assistant for high school students.

Every time you continue the story:
- write exactly one new story chapter
- keep it short, vivid, and easy to read
- end with exactly three numbered choices

Important:
- each chapter should be at most 2 short paragraphs
- the three choices should be clearly numbered
- do not ask the user to type anything
- do not explain the rules
"""


def format_story_for_markdown(story_text: str) -> str:
    if not story_text.strip():
        return "_Your story will appear here._"
    return story_text.replace("\n", "  \n")


def generate_turn(story_state: dict, choice_index: int | None = None):
    if choice_index is not None:
        story_state["story"] += f"\nThe user chose option {choice_index}.\n"

    user_prompt = f"""Here is the story so far:

{story_state["story"]}

Continue the story with one new chapter and then exactly three numbered choices.
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    )

    chapter = response["message"]["content"].strip()
    story_state["story"] += "\n" + chapter + "\n"

    return format_story_for_markdown(story_state["story"]), chapter, story_state


def start_story(story_idea: str):
    if not story_idea.strip():
        empty_state = {"story": ""}
        return "Please enter a story idea first.", "", empty_state

    story_state = {"story": f"Story idea: {story_idea.strip()}\n"}
    return generate_turn(story_state)


def continue_story(choice_index: int, story_state: dict):
    if not story_state["story"].strip():
        return "Start a story first.", "", story_state

    return generate_turn(story_state, choice_index=choice_index)


with gr.Blocks() as demo:
    gr.Markdown("# Interactive Storytelling App")
    gr.Markdown("Start with an idea, then guide the story by clicking one of the three options.")

    story_state = gr.State({"story": ""})

    with gr.Row():
        idea_input = gr.Textbox(
            label="Story idea",
            lines=3,
            placeholder="For example: A dragon wants to win a baking contest.",
        )
        start_button = gr.Button("Start Story", variant="primary")

    full_story_box = gr.Markdown("_Your story will appear here._")
    latest_chapter_box = gr.Textbox(label="Latest chapter and choices", lines=14)

    with gr.Row():
        option_1_button = gr.Button("Choose Option 1")
        option_2_button = gr.Button("Choose Option 2")
        option_3_button = gr.Button("Choose Option 3")

    start_button.click(
        start_story,
        inputs=idea_input,
        outputs=[full_story_box, latest_chapter_box, story_state],
    )

    option_1_button.click(
        lambda state: continue_story(1, state),
        inputs=story_state,
        outputs=[full_story_box, latest_chapter_box, story_state],
    )
    option_2_button.click(
        lambda state: continue_story(2, state),
        inputs=story_state,
        outputs=[full_story_box, latest_chapter_box, story_state],
    )
    option_3_button.click(
        lambda state: continue_story(3, state),
        inputs=story_state,
        outputs=[full_story_box, latest_chapter_box, story_state],
    )


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8080)
