# Image Generation

So far, our AI systems mostly answered with words.
Now we switch to a very different kind of model, one that creates pixels.

For this chapter, we use a lighter modern image model:

- `segmind/SSD-1B`

This model is based on the SDXL family, but it is much smaller and faster than the bigger image models we tested.
That makes it a better fit for the workshop VMs.

This chapter is about **diffusion models**.
The basic idea is surprisingly strange and surprisingly clever.

Very roughly, a diffusion model works like this:

1. It starts with random noise
2. It removes the noise step by step
3. At each step, it tries to move closer to the text prompt
4. After the last step, you get an image

So you can imagine it as a model that slowly turns static into a picture.

That is why the number of steps matters.

- fewer steps, faster, but sometimes rougher
- more steps, slower, but often cleaner

Another important setting is **guidance scale**.
This controls how strongly the model tries to follow your prompt.

- lower guidance, more freedom, sometimes more creative
- higher guidance, more obedient, but sometimes more rigid or strange

## What you will do

- write your own image prompt
- generate one image
- choose the number of steps
- choose the guidance scale
- generate a small comparison grid
- save the results as PNG files

## What the most important settings mean

### `prompt`

This is the text description of the image you want.

Example:

```python
"A tiny robot serving waffles in a sunny university cafe, cartoon style"
```

### `num_inference_steps`

This is the number of denoising steps.

For this chapter, a good range is:

- `10`
- `20`
- `30`

Start with `20`.

### `guidance_scale`

This controls how strongly the image model should follow the prompt.

For this chapter, a good range is:

- `5.0`
- `7.5`
- `10.0`

Start with `7.5`.

### `seed`

The seed controls randomness.

If you keep the same prompt and same settings, the same seed gives a very similar result again.
If you change the seed, you get a different image.

### Why the script uses CPU offload

Even this smaller model is still a real diffusion pipeline.
To keep memory usage comfortable on the workshop VM, the script uses CPU offload and a few VAE memory-saving settings behind the scenes.

## Step 1, open the script

Open:

[`image-generation.py`](/root/genai-workshop/06-image-generation/image-generation.py)

## Step 2, fix the TODOs

There are four small fixes to make.

### TODO 1, write your prompt

Find:

```python
PROMPT = ""
```

Replace it with your own prompt.

Example:

```python
PROMPT = "A tiny robot serving waffles in a sunny university cafe, cartoon style"
```

### TODO 2, choose the main number of steps

Find:

```python
NUM_INFERENCE_STEPS = 0
```

Replace it with a value such as:

```python
NUM_INFERENCE_STEPS = 20
```

### TODO 3, choose the main guidance scale

Find:

```python
GUIDANCE_SCALE = 0.0
```

Replace it with a value such as:

```python
GUIDANCE_SCALE = 7.5
```

### TODO 4, create the comparison lists

Find:

```python
STEP_VALUES = []
GUIDANCE_VALUES = []
```

Replace them with:

```python
STEP_VALUES = [10, 20, 30]
GUIDANCE_VALUES = [5.0, 7.5, 10.0]
```

This will generate a comparison grid so you can see what changing both settings actually does.

## Step 3, run the script

```bash
/root/genai-workshop/.venv/bin/python /root/genai-workshop/06-image-generation/image-generation.py
```

The first run may take a while because the image model has to download.

## Step 4, open the generated images

The script saves its results in:

[`outputs/`](/root/genai-workshop/06-image-generation/outputs)

You should get:

- `generated-image.png`
- `steps-and-guidance-grid.png`

Click those files in VS Code to open them.

## What to look for

When you compare the images, ask yourself:

- does `10` steps already look good?
- how much cleaner is `30` than `10`?
- which guidance value follows the prompt best?
- when does a higher guidance scale start to look too forced?

That is exactly the kind of tradeoff engineers often make.

## Try your own experiments

- change the prompt style, for example `pixel art`, `comic book`, `watercolor`
- change the seed
- change the image size
- try a vague prompt and then a very detailed prompt
- try very low guidance and then very high guidance

You can also monitor GPU usage in another terminal:

```bash
nvidia-smi
```

## What this teaches you

This chapter is not only about making cool pictures.
It also shows that AI systems come in very different forms:

- language models generate text token by token
- diffusion models generate images through repeated denoising steps

Different model families solve different kinds of problems.

## Why this chapter matters

Until now, the workshop generated mainly text.
This chapter shows that generative AI can also create entirely new images from scratch.

It is also the first time students meet a model that does not answer with words, but with pixels.
