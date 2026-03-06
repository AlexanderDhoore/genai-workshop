# Open-Vocabulary Object Detection

This optional chapter is about a different kind of machine vision task:

- not image captioning
- not question answering
- not image generation

Instead, the model tries to **find specific objects in an image**.

The interesting part is that the object names are given in normal language.
So you are not limited to a tiny fixed list of labels.

That is why this is called **open-vocabulary object detection**.
You describe what you want to find, and the model looks for it.

## What you will build

A small Gradio app using **Grounding DINO**.

You will:

- upload an image
- type the objects you want to detect
- let the model draw boxes around matching objects

## Important prompt rule

Grounding DINO expects the object names in a special format:

- lowercase
- each target ends with a period

Example:

```text
pineapple. apple. mango.
```

## Step 1, open the script

Open:

[`open-vocabulary-detection-app.py`](/root/genai-workshop/13-open-vocabulary-detection/open-vocabulary-detection-app.py)

## Step 2, fix the TODO

There is one small fix to make.

Find:

```python
prompt = ""  # TODO
```

Replace it so the script uses the text from the textbox, converts it to lowercase, and makes sure it ends with a period.

## Step 3, run the script

```bash
/root/genai-workshop/.venv/bin/python /root/genai-workshop/13-open-vocabulary-detection/open-vocabulary-detection-app.py
```

Then open:

```text
http://127.0.0.1:8080
```

## Step 4, try the example image

This chapter reuses an earlier workshop image:

[`../05-vision-models/examples/pineapple.png`](/root/genai-workshop/05-vision-models/examples/pineapple.png)

Upload that image first and try prompts like:

```text
pineapple.
apple.
pineapple. apple.
```

## What to try next

- upload your own photo
- try one object name
- try several object names together
- try a strange or unusual object name and see what happens

## What this teaches you

This chapter shows another way language and vision can work together.
The model is not describing the whole image.
Instead, language acts like a search query inside the image.

That is useful in robotics, photo search, industrial inspection, and many other settings where you want to find something specific.

## Why this chapter matters

This chapter shows that language can be used to **control what the vision model looks for**.

That feels very different from ordinary image classification, and it is a fun example of how flexible modern AI models can be.
