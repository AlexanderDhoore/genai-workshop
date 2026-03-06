from pathlib import Path

import torch
from diffusers import AutoPipelineForInpainting
from PIL import Image

MODEL_NAME = "diffusers/stable-diffusion-xl-1.0-inpainting-0.1"

SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_IMAGE_PATH = SCRIPT_DIR.parent / "11-image-editing-and-inpainting" / "examples" / "input.png"
MASK_IMAGE_PATH = SCRIPT_DIR.parent / "11-image-editing-and-inpainting" / "examples" / "mask.png"

PROMPT = "Replace the masked area with a bright green alien face, cartoon style."
STRENGTH = 0.95

GUIDANCE_SCALE = 8.0
NUM_INFERENCE_STEPS = 20
SEED = 42
WIDTH = 512
HEIGHT = 512

assert torch.cuda.is_available(), "This chapter expects a CUDA GPU."
assert INPUT_IMAGE_PATH.exists(), f"Input image not found: {INPUT_IMAGE_PATH}"
assert MASK_IMAGE_PATH.exists(), f"Mask image not found: {MASK_IMAGE_PATH}"

OUTPUT_DIR = SCRIPT_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

print(f"Loading model: {MODEL_NAME}")
pipe = AutoPipelineForInpainting.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    variant="fp16",
)
pipe.enable_model_cpu_offload()
pipe.vae.enable_slicing()
pipe.vae.enable_tiling()

input_image = Image.open(INPUT_IMAGE_PATH).convert("RGB").resize((WIDTH, HEIGHT))
mask_image = Image.open(MASK_IMAGE_PATH).convert("L").resize((WIDTH, HEIGHT))

print()
print("Editing the image...")
edited_image = pipe(
    prompt=PROMPT,
    image=input_image,
    mask_image=mask_image,
    strength=STRENGTH,
    guidance_scale=GUIDANCE_SCALE,
    num_inference_steps=NUM_INFERENCE_STEPS,
    width=WIDTH,
    height=HEIGHT,
    generator=torch.Generator("cuda").manual_seed(SEED),
).images[0]

output_path = OUTPUT_DIR / "edited-image.png"
edited_image.save(output_path)

print()
print("Done.")
print(f"Input image: {INPUT_IMAGE_PATH}")
print(f"Mask image: {MASK_IMAGE_PATH}")
print(f"Edited image: {output_path}")
