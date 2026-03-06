import tempfile

import gradio as gr
import soundfile as sf
from kokoro import KPipeline

SUPPORTED_VOICES = [
    "af_heart",
    "af_bella",
    "af_nicole",
    "af_sarah",
    "af_sky",
    "bf_emma",
    "bf_isabella",
    "bm_george",
    "bm_lewis",
]

print("Loading Kokoro pipeline...")
pipeline = KPipeline(lang_code="a")


def generate_speech(text: str, voice: str):
    if not text.strip():
        return "Please enter some text first.", None

    generator = pipeline(text, voice=voice)

    for _, _, audio in generator:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            sf.write(tmp_file.name, audio, 24000)
            return "Here is your generated speech.", tmp_file.name

    return "No audio was generated.", None


demo = gr.Interface(
    fn=generate_speech,
    inputs=[
        gr.Textbox(
            lines=4,
            label="Text",
            placeholder="Enter a sentence to speak...",
        ),
        gr.Dropdown(
            choices=SUPPORTED_VOICES,
            value="af_heart",
            label="Voice",
        ),
    ],
    outputs=[
        gr.Textbox(label="Status"),
        gr.Audio(label="Generated speech"),
    ],
    title="Kokoro Text to Speech",
    description="Type text, choose a voice, and let Kokoro speak.",
    examples=[
        ["Welcome to the generative AI workshop. Today we are making computers speak.", "af_heart"],
    ],
)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8080)
