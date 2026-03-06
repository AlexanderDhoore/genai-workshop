from pathlib import Path

import matplotlib.pyplot as plt
import torch
from diffusers import StableDiffusionXLPipeline

MODEL_NAME = "segmind/SSD-1B"

# TODO: Write your own prompt.
PROMPT = ""

# TODO: Choose a value such as 10, 20, or 30.
NUM_INFERENCE_STEPS = 0

# TODO: Choose a value such as 5.0, 7.5, or 10.0.
GUIDANCE_SCALE = 0.0

SEED = 42
WIDTH = 512
HEIGHT = 512

# TODO: Create short lists such as [10, 20, 30] and [5.0, 7.5, 10.0].
STEP_VALUES = []
GUIDANCE_VALUES = []

assert torch.cuda.is_available(), "This chapter expects a CUDA GPU."
assert PROMPT.strip(), "Fill in PROMPT before running the script."
assert 1 <= NUM_INFERENCE_STEPS <= 50, "NUM_INFERENCE_STEPS must be between 1 and 50."
assert GUIDANCE_SCALE > 0.0, "GUIDANCE_SCALE must be greater than 0."
assert STEP_VALUES, "Fill in STEP_VALUES before running the script."
assert GUIDANCE_VALUES, "Fill in GUIDANCE_VALUES before running the script."

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

print(f"Loading model: {MODEL_NAME}")
pipe = StableDiffusionXLPipeline.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    use_safetensors=True,
    variant="fp16",
)
pipe.enable_model_cpu_offload()
pipe.vae.enable_slicing()
pipe.vae.enable_tiling()

print()
print("Generating the main image...")
image = pipe(
    prompt=PROMPT,
    num_inference_steps=NUM_INFERENCE_STEPS,
    guidance_scale=GUIDANCE_SCALE,
    width=WIDTH,
    height=HEIGHT,
    generator=torch.Generator("cuda").manual_seed(SEED),
).images[0]

generated_image_path = OUTPUT_DIR / "generated-image.png"
image.save(generated_image_path)

print("Generating the steps-and-guidance grid...")
grid_width = 256
grid_height = 256

fig, axes = plt.subplots(
    len(STEP_VALUES),
    len(GUIDANCE_VALUES),
    figsize=(3 * len(GUIDANCE_VALUES), 3 * len(STEP_VALUES)),
)

if len(STEP_VALUES) == 1 and len(GUIDANCE_VALUES) == 1:
    axes = [[axes]]
elif len(STEP_VALUES) == 1:
    axes = [axes]
elif len(GUIDANCE_VALUES) == 1:
    axes = [[axis] for axis in axes]

for row, steps in enumerate(STEP_VALUES):
    for col, guidance in enumerate(GUIDANCE_VALUES):
        grid_image = pipe(
            prompt=PROMPT,
            num_inference_steps=steps,
            guidance_scale=guidance,
            width=grid_width,
            height=grid_height,
            generator=torch.Generator("cuda").manual_seed(SEED),
        ).images[0]

        axis = axes[row][col]
        axis.imshow(grid_image)
        axis.axis("off")
        axis.set_title(f"{steps} steps\nscale {guidance}")

fig.suptitle("Diffusion comparison, steps and guidance scale")
fig.tight_layout()

comparison_path = OUTPUT_DIR / "steps-and-guidance-grid.png"
fig.savefig(comparison_path, bbox_inches="tight")
plt.close(fig)

print()
print("Done.")
print(f"Main image: {generated_image_path}")
print(f"Comparison image: {comparison_path}")
print()
print("Open the PNG files in VS Code to look at the results.")
