# Music Generation with MusicGen

This chapter asks a fun question:

what if a model does not generate words or speech, but an actual piece of music?

That is what MusicGen does.
You describe a musical idea in words, and the model generates a short audio clip.

We keep it simple:

- one text prompt
- one model dropdown
- one clip length slider

## Which model to use

This chapter includes two model options:

- `Small (300M)`, the default, faster and better for the workshop
- `Medium (1.5B)`, slower, but sometimes nicer

Start with **Small**.

That is the practical default for this VM.

## Step 1, open the script

Open:

[`music-generation-app.py`](/root/genai-workshop/10-music-generation/music-generation-app.py)

## Step 2, fix the TODO

There is one small fix to make.

Find:

```python
max_new_tokens = 0  # TODO
```

Replace it with a value based on `length_seconds`.

Tip:

- MusicGen uses roughly `50` tokens per second

So a good line is:

```python
max_new_tokens = int(length_seconds * 50)
```

## Step 3, run the script

```bash
/root/genai-workshop/.venv/bin/python /root/genai-workshop/10-music-generation/music-generation-app.py
```

Then open:

```text
http://127.0.0.1:8080
```

## What to try

- `A calm piano melody with rain in the background`
- `Energetic synthwave music with retro arcade vibes`
- `A dramatic movie soundtrack with drums and strings`
- `A happy chiptune loop for a video game`

## Practical advice

- start with the **Small** model
- start with about **5 to 10 seconds**
- only try the **Medium** model if you have extra time

## What this teaches you

Music generation is a good reminder that generative AI is not one single technology.
Different model families can work on:

- language
- pictures
- speech
- music

The common idea is generation, but the outputs are very different.

## Why this chapter matters

This chapter shows that generative AI is not limited to words, pictures, or speech.

It can also create entirely new music from a text description.
