import gradio as gr
import whisper

MODEL_NAME = "base"

LANGUAGES = {
    "English": "en",
    "Dutch (Nederlands)": "nl",
    "French (Français)": "fr",
    "German (Deutsch)": "de",
    "Spanish (Español)": "es",
}

print(f"Loading Whisper model: {MODEL_NAME}")
model = whisper.load_model(MODEL_NAME)


def transcribe(audio_path: str | None, language_name: str) -> str:
    if audio_path is None:
        return "Please record or upload an audio clip first."

    language_code = ""  # TODO: look up the selected language in LANGUAGES
    result = model.transcribe(audio_path, language=language_code)
    return result["text"].strip()


demo = gr.Interface(
    fn=transcribe,
    inputs=[
        gr.Audio(type="filepath", label="Record or upload audio"),
        gr.Dropdown(
            choices=list(LANGUAGES.keys()),
            value="English",
            label="Language",
        ),
    ],
    outputs=gr.Textbox(label="Transcribed text", lines=8),
    title="Whisper Audio Transcription",
    description="Upload a short audio clip and turn speech into text with Whisper.",
    examples=[
        ["/root/genai-workshop/08-audio-transcription/examples/example.wav", "English"],
    ],
)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8080)
