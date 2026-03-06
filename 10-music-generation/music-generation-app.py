import gradio as gr
import numpy as np
import scipy.io.wavfile
from transformers import pipeline

MODEL_OPTIONS = {
    "Small (300M)": "facebook/musicgen-small",
    "Medium (1.5B)": "facebook/musicgen-medium",
}


def generate_music(prompt: str, model_name: str, length_seconds: int):
    if not prompt.strip():
        return None

    model_id = MODEL_OPTIONS[model_name]
    synthesiser = pipeline("text-to-audio", model=model_id)

    max_new_tokens = 0  # TODO: estimate this from length_seconds
    result = synthesiser(
        prompt,
        forward_params={"do_sample": True, "max_new_tokens": max_new_tokens},
    )

    audio = result["audio"][0] if isinstance(result["audio"], list) else result["audio"]
    audio = np.asarray(audio).squeeze()
    sampling_rate = result["sampling_rate"]
    scipy.io.wavfile.write("generated-music.wav", rate=sampling_rate, data=audio)
    return sampling_rate, audio


demo = gr.Interface(
    fn=generate_music,
    inputs=[
        gr.Textbox(
            lines=2,
            label="Prompt",
            placeholder="For example: Energetic synthwave music with retro arcade vibes",
        ),
        gr.Dropdown(
            choices=list(MODEL_OPTIONS.keys()),
            value="Small (300M)",
            label="Model",
        ),
        gr.Slider(
            minimum=5,
            maximum=30,
            step=1,
            value=10,
            label="Clip length (seconds)",
        ),
    ],
    outputs=gr.Audio(type="numpy", label="Generated music"),
    title="MusicGen Text to Music",
    description="Write a musical prompt and generate a short audio clip.",
)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8080)
