# Image Editing and Inpainting

Chapter 6 generated a completely new image from scratch.
This chapter does something more controlled.

It changes only part of an existing image.
That is called **inpainting**.

The basic idea is simple:

- you start with an image
- you provide a mask
- white areas in the mask are the parts the model is allowed to change
- black areas are the parts it should keep

So this chapter is different from chapter 6:

- chapter 6 generated a whole new image from text
- chapter 11 edits only a selected part of an image

## What you will use

We use an SDXL inpainting model:

- `diffusers/stable-diffusion-xl-1.0-inpainting-0.1`

This turned out to be practical on the workshop VM.
It is much lighter than the `Z-Image-Turbo` path we tested earlier.

## What you will do

- use a provided example image
- use a provided mask
- write a prompt describing the change
- choose the edit strength
- save the edited result

## Step 1, look at the example files

This chapter includes:

- [`examples/input.png`](/root/genai-workshop/11-image-editing-and-inpainting/examples/input.png)
- [`examples/mask.png`](/root/genai-workshop/11-image-editing-and-inpainting/examples/mask.png)

Open both in VS Code.

Notice:

- the input image contains a simple orange shape
- the mask has one white circle
- only that white circle should be edited

## Step 2, open the script

Open:

[`image-inpainting.py`](/root/genai-workshop/11-image-editing-and-inpainting/image-inpainting.py)

## Step 3, fix the TODOs

There are two small fixes to make.

### TODO 1, write the editing prompt

Find:

```python
PROMPT = ""
```

Replace it with something visual.

Example:

```python
PROMPT = "Replace the masked area with a bright green alien face, cartoon style."
```

### TODO 2, choose the edit strength

Find:

```python
STRENGTH = 0.0
```

Try:

```python
STRENGTH = 0.95
```

Higher strength means the masked region can change more aggressively.

## Step 4, run the script

```bash
/root/genai-workshop/.venv/bin/python /root/genai-workshop/11-image-editing-and-inpainting/image-inpainting.py
```

The first run may take a while because the inpainting model has to download.

## Step 5, open the edited image

The script saves the result in:

[`outputs/edited-image.png`](/root/genai-workshop/11-image-editing-and-inpainting/outputs/edited-image.png)

## What to try

- try a different object in the masked area
- try a realistic style and then a cartoon style
- change the strength a little
- make the prompt very specific and then very vague

## What this teaches you

Generative image models are not only useful for making posters and fantasy scenes.
They can also be used as editing tools.

That is much closer to how creative software is often used in practice:
adjust one region, keep the rest, and iterate.

## Why this chapter matters

This chapter shows that image models do not only create new pictures.
They can also **modify existing images**, which is useful for editing, design, and creative experiments.
