# Multi-Step Story Generation

In chapter 2, you asked the model to write one story in one go.
That works, but it is not always the best strategy.

If a task is bigger, longer, or more structured, one huge prompt often gives messy results.
So in this chapter we do what good engineers usually do, we break the problem into smaller parts.

Instead of asking the model to write everything at once, we split the job into smaller steps:

1. generate a short plan
2. write one part at a time
3. keep passing the story-so-far back into the model

This is one of the key ideas behind many real AI applications.
The model does not magically remember everything for you, so your code has to manage the structure.

## What you will do

- choose a story idea
- generate a list of story parts
- fix the code that parses those parts
- fix the code that keeps the story context
- compare normal mode and thinking mode
- run the full script and inspect the result

## Step 1, open the script

Open:

[`story-generation.py`](/root/genai-workshop/03-multi-step-generation/story-generation.py)

This script is close to working, but it still has a few TODOs.

## Step 2, choose a story idea

Find:

```python
STORY_IDEA = ""
```

Replace it with your own idea.

Examples:

```python
STORY_IDEA = "A robot falls in love with a toaster."
STORY_IDEA = "A fox discovers a glowing stone in the forest."
STORY_IDEA = "A spaceship crashes on a planet made entirely of water."
```

## Step 3, fix the outline parsing

The first model call generates a list of short story-part summaries.
But the raw output is only one block of text.

Find this line:

```python
abstracts = []
```

Replace it with code that:

- splits `abstracts_raw` into lines
- removes empty lines
- strips extra whitespace

If you want, you can also strip away simple numbering like `1.` or `-`.

## Step 4, fix the story memory

Later in the script, each part of the story is generated one by one.
To keep the story coherent, you need to accumulate the chapters that already exist.

Find this line:

```python
# full_story_so_far = ...
```

Replace it with code that appends the new chapter text to `full_story_so_far`.

If you do not do this, the model will forget what already happened.

## Step 5, run the script

```bash
/root/genai-workshop/.venv/bin/python /root/genai-workshop/03-multi-step-generation/story-generation.py
```

## Step 6, try thinking mode properly

This is the first chapter where thinking mode really makes sense.

Find:

```python
THINKING_MODE = False
```

First run the script with:

```python
THINKING_MODE = False
```

Then try:

```python
THINKING_MODE = True
```

Compare:

- does the outline improve?
- does the story stay more coherent?
- how much slower does it become?

Some Ollama and model combinations may expose raw thinking text internally.
This script strips that away so you can compare the final story output more cleanly.

## Why thinking mode fits here

Some local models can spend extra effort on reasoning before answering.
In Ollama, that is called **thinking mode**.

It is not magic, and it is not always worth the extra time.
But tasks with planning and structure are exactly the kind of place where it can help.

## What to look for

When the script works, you should see:

- a short outline first
- then multiple story parts
- the later parts should still fit the earlier ones

## Questions to think about

- Is the multi-step version better than one big prompt?
- Does the story stay more coherent when previous chapters are passed back in?
- What happens if you remove the story memory completely?
- When is thinking mode worth the extra time?

## Why this chapter matters

This is a very important pattern in generative AI:

good applications often come from simple pipelines of multiple model calls, not just one giant prompt.
