import gradio as gr
import ollama

MODEL_NAME = "qwen3:4b"
SYSTEM_PROMPT = (
    "You are a playful storytelling assistant for high school students. "
    "Write short, vivid, easy-to-read stories."
)


def generate_story(prompt: str) -> str:
    if not prompt.strip():
        return "Please enter a story idea first."

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )
    return response["message"]["content"]


demo = gr.Interface(
    fn=generate_story,
    inputs=gr.Textbox(
        label="Story idea",
        lines=3,
        placeholder="For example: A lonely robot finds a hidden village in the forest.",
    ),
    outputs=gr.Textbox(label="Generated story", lines=12),
    title="AI Storytelling App",
    description="Turn a short idea into a story using a local language model.",
)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8080)
