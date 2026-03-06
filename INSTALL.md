# Install Notes

This file is for the instructor or for future maintenance work.
It describes what should be installed on the VM image before students start the workshop.

The goal is simple:

- students should not spend the workshop installing heavy software
- most chapters should work with one shared Python environment
- GPU-heavy dependencies should already be present on the VM

## Recommended base setup

Use:

- Linux with NVIDIA drivers working
- Python 3.11
- Ollama installed system-wide
- one shared virtual environment at `/root/genai-workshop/.venv`

Important:

- Do not use Python 3.13 for the shared workshop environment
- At least one workshop dependency, `kokoro`, failed to install on Python 3.13 during verification
- Python 3.11 worked for dependency resolution

## System packages

Install these outside the Python environment:

```bash
apt-get update
apt-get install -y ffmpeg espeak-ng python3-pip python3-virtualenv
```

Why:

- `ffmpeg` is useful for Whisper and audio processing
- `espeak-ng` is useful for text-to-speech related packages
- `python3-virtualenv` lets us create a Python 3.11 environment even when `python3.11 -m venv` is not available

## Ollama

Install Ollama system-wide:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Check:

```bash
ollama --version
systemctl is-active ollama
```

## Shared Python environment

Create the shared environment with Python 3.11:

```bash
cd /root/genai-workshop
python3.11 -m virtualenv .venv
source .venv/bin/activate
```

## Python requirements

Install the shared workshop packages:

```bash
source /root/genai-workshop/.venv/bin/activate
pip install -r /root/genai-workshop/requirements.txt
```

Note:

- this is enough on its own, no separate PyTorch step is needed
- `requirements.txt` includes a tested PyTorch version directly
- on Linux, that install pulls a large CUDA-enabled Torch stack, which is exactly why it should be done while preparing the VM template, not during the workshop
- the workshop currently installs `diffusers` from GitHub, not from the latest PyPI release
- reason: newer image-model support moves quickly, and this matched the verified workshop environment on 2026-03-06

## Recommended Ollama models to pre-pull

At minimum:

```bash
ollama pull qwen3:4b
ollama pull qwen3:1.7b
ollama pull qwen3-vl:4b
```

Optional:

```bash
ollama pull gemma3:1b
ollama pull qwen3-vl:2b
```

## Recommended Hugging Face cache warm-up

These chapters use Hugging Face models, not Ollama models:

- chapter 6 image generation
- chapter 8 audio transcription
- chapter 9 text to speech
- chapter 10 music generation
- chapter 11 image editing and inpainting
- chapter 13 open-vocabulary object detection

To avoid first-run downloads during class, warm those caches on the template VM:

```bash
source /root/genai-workshop/.venv/bin/activate

python - <<'PY'
import whisper
whisper.load_model("base")
PY

python - <<'PY'
from kokoro import KPipeline
KPipeline(lang_code="a")
PY

python - <<'PY'
import torch
from diffusers import StableDiffusionXLPipeline
StableDiffusionXLPipeline.from_pretrained("segmind/SSD-1B", torch_dtype=torch.bfloat16)
PY

python - <<'PY'
import torch
from diffusers import AutoPipelineForInpainting
AutoPipelineForInpainting.from_pretrained(
    "diffusers/stable-diffusion-xl-1.0-inpainting-0.1",
    torch_dtype=torch.bfloat16,
)
PY

python - <<'PY'
from transformers import pipeline
pipeline("text-to-audio", model="facebook/musicgen-small")
pipeline("text-to-audio", model="facebook/musicgen-medium")
PY

python - <<'PY'
from transformers import AutoModelForZeroShotObjectDetection, AutoProcessor
AutoProcessor.from_pretrained("IDEA-Research/grounding-dino-base")
AutoModelForZeroShotObjectDetection.from_pretrained("IDEA-Research/grounding-dino-base")
PY
```

The music chapter defaults to `facebook/musicgen-small`, but the chapter also exposes `facebook/musicgen-medium` as an optional choice, so cache both if you want a fully prewarmed template.

## Hugging Face model cache

Ollama stores its own models, but the diffusion and audio chapters also download Hugging Face models.

Important practical note:

- the default `/root/.cache/huggingface` location can fill up quickly on a small VM disk
- image generation models are much larger than the Ollama text models

Recommended:

- give the VM image a larger disk if possible
- or set a separate cache location with more space

Example:

```bash
export HF_HOME=/srv/hf-cache
mkdir -p "$HF_HOME"
```

Practical finding from testing on this VM:

- `Tongyi-MAI/Z-Image-Turbo` looked attractive, but it was not a good default on the earlier 32 GB root disk
- it required the development version of `diffusers`
- after the VM disk was expanded to 128 GB, it became practical again
- its download is large, so it should be pre-downloaded onto the workshop VM image
- on the RTX 4000 SFF Ada 20 GB GPU, it did not fit with a naive `.to("cuda")` load
- it did work with `enable_model_cpu_offload()` plus VAE slicing and tiling
- verified chapter 6 settings:
  - `torch_dtype=torch.bfloat16`
  - `guidance_scale=0.0`
  - `num_inference_steps=9`
  - `width=512`
  - `height=512`
- measured verified behavior on this VM after caching:
  - model load about 32 seconds
  - 512x512 generation about 22 seconds
  - peak GPU allocation about 11.7 GiB
- the bigger problem was system RAM, not just VRAM, because CPU offload pushed memory usage too high for a comfortable classroom default
- `segmind/SSD-1B` turned out to be the better default for chapter 6
- verified behavior for `segmind/SSD-1B` on this VM:
  - ungated, no Hugging Face auth needed
  - about 45 seconds first cached load in the one-image test
  - about 4.8 seconds for one 512x512 image at 20 steps
  - about 2.6 GiB peak GPU allocation
  - about 6.5 GiB peak process RSS
- keep `Tongyi-MAI/Z-Image-Turbo` as an optional instructor demo or future bonus model, not the default student path

## Verification workflow

When a new chapter script is created or edited:

- keep a verified solution version in a `-solution` folder when useful
- run the script locally before considering the chapter finished
- record any extra system-level dependencies here in this file

Chapter 1 verification target:

```bash
source /root/genai-workshop/.venv/bin/activate
python /root/genai-workshop/01-first-language-model-solution/first-local-llm.py
```
