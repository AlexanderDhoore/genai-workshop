# Text to Speech with Kokoro

In the previous chapter, AI listened to speech and turned it into text.
Now we do the reverse.

This chapter is about **text-to-speech**, often shortened to **TTS**.
That means a model takes written text and generates spoken audio.

We use `Kokoro` because it is still a very good fit for this workshop:

- simple to run locally
- good enough quality to sound impressive
- easy to wrap in a Gradio app

There are newer text-to-speech models, but many of them are heavier or more awkward to set up.
For this workshop, Kokoro is still the pragmatic choice.

## What you will build

A small Gradio app that:

- takes text as input
- lets you choose a voice
- generates spoken audio

## Step 1, open the script

Open:

[`text-to-speech-app.py`](/root/genai-workshop/09-text-to-speech/text-to-speech-app.py)

## Step 2, fix the TODO

There is one small fix to make.

Find:

```python
voice=""  # TODO
```

Replace it so the model really uses the selected voice from the dropdown.

## Step 3, run the script

```bash
/root/genai-workshop/.venv/bin/python /root/genai-workshop/09-text-to-speech/text-to-speech-app.py
```

Then open:

```text
http://127.0.0.1:8080
```

## Step 4, try a first sentence

Try something like:

```text
Welcome to the generative AI workshop. Today we are making computers speak.
```

Then change the voice and listen again.

## Important note about the first run

The first run can take a little longer because Kokoro may download some extra files.
After that, it should be much faster.

## What to try

- a short welcome message
- a funny sentence
- something dramatic
- the same sentence with different voices

## What this teaches you

Text and speech can be converted in both directions:

- Whisper turns speech into text
- Kokoro turns text into speech

Put those ideas together, and you are already close to a simple voice assistant.

## Why this chapter matters

This chapter shows that generative AI can also **produce audio**, not just text or images.

It is a nice companion to the Whisper chapter:

- Whisper turns speech into text
- Kokoro turns text into speech
