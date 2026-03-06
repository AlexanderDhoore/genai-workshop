# Turn Your LLM Into a Storyteller

In chapter 1, the model already answered a prompt.
Now we make the next step, we learn how to **steer** it.

This chapter is about **prompting**.
Prompting means giving the model instructions in a smart way so it behaves how you want.

The key idea is that prompts have structure:

- the `system` prompt tells the model what kind of assistant it should be
- the `user` prompt gives the actual request

With only a few small changes, the same model can behave like a storyteller, a pirate, a sci-fi writer, or a dramatic fantasy narrator.
That is powerful because we are not retraining the model, we are just guiding it with language.

## What you will do

- open a small Python script
- fix two TODOs
- run the script with the shared workshop environment
- compare how the output changes when you edit the prompts

## Step 1, open the script

Open:

[`storytelling-assistant.py`](/root/genai-workshop/02-storytelling-assistant/storytelling-assistant.py)

This script is almost ready, but not completely.
You need to fix it first.

## Step 2, fix the TODOs

There are two small things to fix:

### TODO 1

Fill in your own creative story idea:

```python
USER_PROMPT = ""
```

Examples:

```python
USER_PROMPT = "A lonely robot discovers a hidden village in the forest."
USER_PROMPT = "An astronaut finds a message in a bottle on Mars."
USER_PROMPT = "A squirrel accidentally becomes the captain of a pirate ship."
```

### TODO 2

Inside the `messages` list, the user message is still broken.
You need to send the contents of `USER_PROMPT` to the model.

If you fix both TODOs correctly, the script should generate a story.

## Step 3, run the script

Use the shared workshop environment:

```bash
/root/genai-workshop/.venv/bin/python /root/genai-workshop/02-storytelling-assistant/storytelling-assistant.py
```

## Step 4, experiment

Now start changing the prompts and see what happens.

Try changing the system prompt so the model becomes:

- a fantasy writer
- a science fiction writer
- a silly storyteller for children
- a mysterious dungeon master

You can also try changing the user prompt while keeping the system prompt fixed.

That lets you see the difference between:

- changing the model's role
- changing the request you give to that role

## What this teaches you

Real AI products often feel different even when they use the same model under the hood.
That is often because of prompting:

- one app uses a serious system prompt
- another uses a playful one
- another adds formatting rules or safety rules

So prompting is part of product design, not just coding.

## Questions to think about

- Which has the biggest effect, the system prompt or the user prompt?
- Can you make the same story idea feel funny, dramatic, or poetic just by changing the instructions?
- Does the model follow your style instructions well, or only partly?

## Why this chapter matters

This is one of the most important ideas in the whole workshop:

you do not need to train a model yourself to make it behave differently.
Often, a carefully written prompt is already enough to create a completely different experience.
