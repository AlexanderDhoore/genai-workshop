# Audio Transcription with Whisper

This is the first optional chapter after the main workshop path.

Until now, most inputs in the workshop were text or images.
Now we work with sound.

The app stays simple:

- upload or record audio
- choose a language
- get text back

We use OpenAI Whisper for this.
Whisper is a speech-to-text model, which means it listens to spoken audio and turns it into words.
That is useful for subtitles, meeting notes, voice interfaces, accessibility tools, and more.

## What you will build

A small Gradio app that:

- accepts an audio file or microphone recording
- lets you choose a language
- transcribes speech into text

## Step 1, open the script

Open:

[`audio-transcription-app.py`](/root/genai-workshop/08-audio-transcription/audio-transcription-app.py)

## Step 2, fix the TODO

There is one small fix to make.

Find:

```python
language_code = ""  # TODO
```

Replace it so the selected language name is converted into the correct short language code from the `LANGUAGES` dictionary.

## Step 3, run the script

```bash
/root/genai-workshop/.venv/bin/python /root/genai-workshop/08-audio-transcription/audio-transcription-app.py
```

Then open:

```text
http://127.0.0.1:8080
```

## Step 4, try the example audio

This chapter includes a ready-made test file:

[`examples/example.wav`](/root/genai-workshop/08-audio-transcription/examples/example.wav)

Upload that file first so you can confirm the app works before trying your own recording.

## About microphone input

Uploading audio files should work normally.

Microphone input can be trickier in browsers:

- many browsers only allow microphone access on secure HTTPS pages
- if you open the app through plain HTTP, microphone recording may be blocked

So for the workshop, **uploading a file is the safest default path**.

## What this teaches you

This is a nice reminder that AI input does not have to be typed by a human.
It can come from a microphone, a phone recording, a video soundtrack, or an interview.

Once speech becomes text, all the earlier text-based tools become possible again.

## Why this chapter matters

Until now, most of the workshop used text prompts.
This chapter shows that generative AI can also listen to speech and turn it into text.

That opens the door to voice assistants, subtitles, meeting notes, and many other applications.
