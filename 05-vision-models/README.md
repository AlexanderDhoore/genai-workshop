# Vision Models, Images as Input

Until now, the model only received text.
In this chapter, we let it look at an image as well.

That kind of model is called a **vision-language model**, or **VLM**.
It combines two skills:

- understanding images
- understanding language

That means the model can answer questions like:

- What is in this image?
- Is this indoors or outdoors?
- What object do you see?
- What text appears in the image?

We will use a modern vision-language model:

- `qwen3-vl:4b`

This model can handle both text and images, and it is still small enough to run comfortably on the workshop GPU machines.

## What you will do

- use a provided example image
- fix a small script
- ask a vision model questions about the image
- optionally try your own image afterward

## Step 1, look at the example images

This chapter includes a few example images in:

[`examples/`](/root/genai-workshop/05-vision-models/examples)

You can start with one of those, so you do not need to find your own image yet.

The folder currently contains:

- `pineapple.png`, a fruit photo
- `cucumber.png`, another simple object photo
- `milk.png`, a product image
- `receipt.png`, a small document-style image with readable text

Later, if you want, you can drag your own image into this folder in VS Code and use that instead.

If you click an image file in VS Code, it will open a preview so you can see what the model is looking at.

## Step 2, open the script

Open:

[`vision-question-answering.py`](/root/genai-workshop/05-vision-models/vision-question-answering.py)

This script sends both:

- a text question
- an image path

to the local model.

## Step 3, fix the TODOs

There are two small fixes to make.

### TODO 1, choose an image

Find:

```python
IMAGE_PATH = ""
```

Replace it with one of the example images, for example:

```python
IMAGE_PATH = "examples/pineapple.png"
```

### TODO 2, actually pass the image to the model

Find this broken line:

```python
"images": []  # TODO
```

Replace it so the model really receives the selected image path.

If you forget this part, the model will only see your text prompt and not the image.

## Step 4, run the script

```bash
/root/genai-workshop/.venv/bin/python /root/genai-workshop/05-vision-models/vision-question-answering.py
```

If the model is not downloaded yet, pull it once:

```bash
ollama pull qwen3-vl:4b
```

## Step 5, experiment

Once it works, try changing the question:

- `What object do you see?`
- `Describe this image in one sentence.`
- `What colors are visible?`
- `Is this a fruit, a drink, or something else?`

Then try your own image.

## Optional extra, try the receipt example

Set:

```python
IMAGE_PATH = "examples/receipt.png"
```

Then ask:

- `What text can you read?`
- `Summarize this document in 3 bullet points.`
- `What is the date on this paper?`
- `What is the total price?`

After that, you can also try your own receipt, menu, poster, or school document photo.

So we are not making a separate document-QA chapter.
Instead, we let the vision model handle it as one of its normal use cases.

## If something goes wrong

### The script says the image does not exist

Check:

- did you type the file name correctly?
- is the image really inside the `examples/` folder?
- did you use the right extension, like `.png` or `.jpg`?

### The answer ignores the image

Then you probably forgot to pass the image path inside the `images` list.

## What this teaches you

This chapter shows that modern AI is not only about chat.
A single model can often do several related tasks:

- describe a photo
- answer questions about what it sees
- read visible text
- summarize a document image

That is why multimodal AI is such a big deal.

## Why this chapter matters

This is the first time the workshop becomes truly multimodal.

The model is no longer just reading text.
Now it can also look at the world through images.
