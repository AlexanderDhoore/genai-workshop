# Interactive Storytelling App

This is the finale of the main workshop.

Until now, each chapter focused on one idea at a time.
Now we combine several of them into one small product.

The app is built around a simple idea:

- a Gradio app
- one chapter at a time
- three buttons for three choices
- the story keeps going based on what the user picks

We also keep this app **text-only on purpose**.

Why:

- it stays lightweight
- it runs comfortably alongside `qwen3:4b`
- students can experiment without fighting GPU memory

So this chapter does **not** generate images inside the app.
The image-generation chapter already showed that part separately.

## What you will build

A small interactive story game:

1. the user enters a story idea
2. the model writes the first chapter
3. the model also gives three possible next actions
4. the user clicks one of the buttons
5. the story continues

This brings together several ideas from the earlier chapters:

- prompting
- multi-step generation
- keeping context between model calls
- building a Gradio app

## Step 1, open the script

Open:

[`interactive-story-app.py`](/root/genai-workshop/07-interactive-story-app/interactive-story-app.py)

## Step 2, fix the TODO

There is one small fix to make.

Find this broken line:

```python
messages=[]  # TODO
```

Replace it with the correct messages list:

- a system message with `SYSTEM_PROMPT`
- a user message with `user_prompt`

Just like in the earlier Ollama chapters.

## Step 3, run the script

```bash
/root/genai-workshop/.venv/bin/python /root/genai-workshop/07-interactive-story-app/interactive-story-app.py
```

Then open:

```text
http://127.0.0.1:8080
```

If you are using the VM from your own laptop, open the forwarded port in VS Code or use the VM IP address.

## What the app does

The script stores the story so far in a small Python dictionary.

Each time you click a choice button:

- the app adds your choice to the story state
- it sends the updated story to the model
- the model writes one new chapter and three new options

So this is a simple example of an **interactive AI loop**.

## What to try

- `A shy robot becomes the goalkeeper of a strange football team.`
- `A student finds a hidden laboratory under the university.`
- `A dragon wants to win a baking contest.`
- `A tiny submarine explores the canals of Bruges.`

## Optional polish, try thinking mode

After the app works, you can experiment with thinking mode as a bonus.

Inside the `ollama.chat(...)` call, recent Ollama versions support:

```python
think=True
```

This can sometimes improve the choices or story logic.
But it also makes the app slower.

So keep it as an optional experiment, not the default.

## What this teaches you

This is a small example of how real AI products are built:

- keep state somewhere
- show the user a simple interface
- call the model repeatedly
- use each answer to decide what happens next

The individual pieces are simple.
The product feeling comes from how those pieces are combined.

## Why this chapter matters

This chapter is the payoff of the core workshop.

It turns the separate ideas from earlier chapters into one small app that feels like a real AI product.
