import gradio as gr
import torch
from PIL import ImageDraw
from transformers import AutoModelForZeroShotObjectDetection, AutoProcessor

MODEL_NAME = "IDEA-Research/grounding-dino-base"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Loading model: {MODEL_NAME}")
processor = AutoProcessor.from_pretrained(MODEL_NAME)
model = AutoModelForZeroShotObjectDetection.from_pretrained(MODEL_NAME).to(DEVICE)


def detect_and_draw(image, text_prompt: str):
    if image is None:
        return None

    prompt = text_prompt.strip().lower()
    if prompt and not prompt.endswith("."):
        prompt += "."

    inputs = processor(images=image, text=prompt, return_tensors="pt").to(DEVICE)

    with torch.no_grad():
        outputs = model(**inputs)

    results = processor.post_process_grounded_object_detection(
        outputs,
        inputs.input_ids,
        threshold=0.4,
        text_threshold=0.3,
        target_sizes=[image.size[::-1]],
    )[0]

    output_image = image.copy()
    draw = ImageDraw.Draw(output_image)

    for box, label, score in zip(results["boxes"], results["labels"], results["scores"]):
        x1, y1, x2, y2 = box.tolist()
        draw.rectangle((x1, y1, x2, y2), outline="red", width=3)
        draw.text((x1, y1), f"{label} ({score:.2f})", fill="white")

    return output_image


demo = gr.Interface(
    fn=detect_and_draw,
    inputs=[
        gr.Image(type="pil", label="Upload an image"),
        gr.Textbox(
            label="Text prompt",
            placeholder="For example: pineapple. apple.",
            info="Use lowercase labels and end each target with a period.",
        ),
    ],
    outputs=gr.Image(type="pil", label="Detected image"),
    title="Open-Vocabulary Object Detection",
    description="Detect objects with Grounding DINO using natural-language labels.",
    examples=[
        ["/root/genai-workshop/05-vision-models/examples/pineapple.png", "pineapple. apple."],
    ],
)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8080)
