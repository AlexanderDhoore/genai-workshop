# Build Your First AI Web App

Until now, everything happened in the terminal.
That is fine for experiments, but real people usually want buttons, text boxes, and a page they can open in a browser.

In this chapter, you will build your first small web interface with **Gradio**.
Gradio is a Python library that lets you turn a normal Python function into a simple website.

That means:

- you write a Python function
- Gradio puts a text box and button around it
- you open the result in your browser

So this chapter is really about one big idea:

your Python code can become a web app with only a few extra lines.

## What you will do

- open a Gradio script
- fix one small TODO
- run the script
- open the web app in your browser
- chat with your local language model through a real interface

## Step 1, open the script

Open:

[`gradio-story-app.py`](/root/genai-workshop/04-first-gradio-app/gradio-story-app.py)

This script creates a tiny storytelling app.

The user types a prompt into a web page, your Python function sends that prompt to the local LLM, and the answer comes back into the page.

## Step 2, understand the main pieces

You do not need to memorize everything, just understand the big picture.

The script has 3 important parts:

### Part 1, the model settings

```python
MODEL_NAME = "qwen3:4b"
SYSTEM_PROMPT = "..."
```

This tells Ollama which model to use and what kind of assistant it should be.

### Part 2, the Python function

```python
def generate_story(prompt):
    ...
```

This is the normal Python function that does the real work.
Gradio will call this function every time the user presses the button in the browser.

### Part 3, the Gradio interface

```python
demo = gr.Interface(...)
```

This is the part that builds the website.
It tells Gradio:

- which function to call
- what inputs to show
- what outputs to show
- what title and description should appear on the page

## Step 3, fix the TODO

There is one small broken line in the script.

Find this:

```python
{"role": "user", "content": ""}  # TODO
```

Replace the empty string with the variable that contains the user's text.

If you fix that correctly, the website should work.

## Step 4, run the app

Run:

```bash
/root/genai-workshop/.venv/bin/python /root/genai-workshop/04-first-gradio-app/gradio-story-app.py
```

After a few seconds, the terminal should show that the server is running.

While the app is running:

- keep that terminal open
- do not expect the terminal prompt to come back yet
- that is normal, the Python script is now acting like a web server

## Step 5, open the website

Open a browser on your own laptop and go to:

```text
http://<your-vm-ip>:8080
```

Replace `<your-vm-ip>` with the IP address of your VM.

If you forgot the IP address, you can check it in the VM terminal with:

```bash
hostname -I
```

If there are multiple addresses, use the one given by your instructor.

## Step 6, try it

Enter prompts like:

- `A shy robot wants to enter a baking contest.`
- `A fox finds a secret tunnel under a castle.`
- `Write a spooky bedtime story about a lighthouse on Mars.`

Then press the button and see what happens.

## Step 7, stop the app

When you are done, go back to the terminal and press:

```text
Ctrl+C
```

That stops the web server.

## If something goes wrong

### The page does not open

Check:

- is the Python script still running?
- did you use the correct VM IP address?
- did you include `:8080` in the browser URL?

### Port 8080 is already in use

That usually means an older Gradio app is still running.

You can stop Python servers with:

```bash
pkill python
```

Then run the script again.

## What this teaches you

This is the point where AI programming starts to feel more like building software for other people.
The same model can be much more usable once it has:

- a simple interface
- a clear input box
- a visible output area

That is often the difference between a demo in a terminal and a tool someone else can actually try.

## Why this chapter matters

This is the first moment where your AI code starts to feel like a real application.

The model is still the same.
The Python is still simple.
But once it appears in a browser, it becomes much easier to share, test, and improve.
