# Hands-On Generative AI Workshop with Local Models: From Local LLMs to Multimodal AI Applications

Welcome to the workshop.

Generative AI is the part of AI that can create things: text, images, speech, music, and interactive experiences.
In this workshop, you will try all of that on a GPU virtual machine.

That is an important idea from the start.
We are not only using giant cloud websites.
We are also learning how to run modern AI models ourselves, with Python code we can understand.

By the end of the workshop, you will have built small examples with:

- local language models
- storytelling and prompting
- image understanding
- image generation and editing
- speech and music
- interactive AI apps

This workshop is hands-on.
You will read short `README.md` files, fix small Python TODOs, and run everything yourself.

## Getting started

Open Visual Studio Code on your laptop and connect to your assigned virtual machine using Remote SSH.
That virtual machine runs on GPU servers at VIVES.

We use this setup because AI models often run much faster on a GPU than on a normal CPU.
GPUs are very good at the kind of large parallel calculations that modern AI models need.

This is also a realistic engineering setup.
Linux and Python are both very popular in data science and AI work, so you are using tools that professionals use too.

You should end up with a VS Code window that shows something like:

```text
SSH: 10.26.x.y
```

Then open the folder:

```text
/root/genai-workshop/
```

This workshop uses plain Markdown files and Python scripts.
That means you can read the explanations, edit the code, and run the files directly from VS Code or the terminal.

## Shared environment

This workshop expects:

- a Linux GPU VM
- VS Code Remote SSH
- Python 3.11
- one shared environment at `/root/genai-workshop/.venv`

A **virtual environment**, or **venv**, is just a self-contained Python setup for one project.
It keeps the workshop libraries together so they do not get mixed up with other Python packages on the system.

If your environment is already prepared, you usually only need to select the correct Python interpreter in VS Code.

If you need to create it manually, the commands look like this:

```bash
cd /root/genai-workshop
python3.11 -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## How to work through the workshop

For each chapter:

1. open the chapter folder
2. read the `README.md`
3. open the Python script
4. fix the small TODOs
5. run the script

Most chapters are designed so that you need to make one or two small fixes before they work.
That is on purpose.
The goal is not only to watch AI, but to understand a little of how the code fits together.

## Core workshop path

These are the main chapters:

### 1. [Run your first local LLM](01-first-language-model)

Learn what a language model is, why local AI matters, and how Ollama lets you run a model from Python.

### 2. [Prompting and storytelling](02-storytelling-assistant)

See how prompts shape the behavior of a model, and turn the same model into a creative storyteller.

### 3. [Multi-step generation](03-multi-step-generation)

Split a bigger task into smaller model calls and see why real AI applications often use pipelines instead of one giant prompt.

### 4. [Build your first AI web app](04-first-gradio-app)

Wrap a local model in a small Gradio interface so your Python script starts to feel like a real product.

### 5. [Vision models, images as input](05-vision-models)

Ask a model questions about images and see what happens when AI can work with both pictures and text.

### 6. [Image generation](06-image-generation)

Generate images from text prompts and learn the basic idea behind diffusion models.

### 7. [Interactive storytelling app](07-interactive-story-app)

Bring everything together in one final interactive app with memory, choices, and multiple model calls.

## Optional chapters

If you have extra time, or if you want to explore more, try these:

### 8. [Audio transcription](08-audio-transcription)

Turn speech into text with Whisper and see how AI can listen as well as write.

### 9. [Text to speech](09-text-to-speech)

Generate spoken audio from text and build the other half of a voice interface.

### 10. [Music generation](10-music-generation)

Create short music clips from text prompts.

### 11. [Image editing and inpainting](11-image-editing-and-inpainting)

Edit part of an image with a mask and a prompt, instead of generating a whole new picture.

### 12. [Tool calling](12-tool-calling)

Let a local language model call a Python tool to answer a real-world question with live data.

### 13. [Open-vocabulary object detection](13-open-vocabulary-detection)

Detect objects in an image by describing them in natural language.

## Solutions

Most chapters also have a matching `-solution` folder.

These are useful if:

- you get stuck
- you want to compare your code with a verified version
- you want to study a clean working example afterward
