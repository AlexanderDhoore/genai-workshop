# Run Your First Local LLM

This chapter is your first real contact with a modern AI model.

We are going to run a **large language model**, often shortened to **LLM**.
An LLM is a model trained on huge amounts of text so it can continue text, answer questions, follow instructions, and imitate styles of writing.

You have probably already used tools like ChatGPT.
The difference here is that we are doing something more interesting for engineers:

- we run the model on our own machine
- we control it from Python
- we can swap models and inspect how they behave

To make that easy, we use **Ollama**.
Ollama is a tool that downloads models, stores them locally, and gives Python an easy way to talk to them.

So the big idea of this chapter is simple:

local AI is real, useful, and surprisingly accessible.

## What you will do

- check that Ollama is available
- pull a small local model
- chat with it in the terminal first
- open a small Python script
- run the same kind of model from Python
- compare a few lightweight models

## Step 1, check that Ollama works

Open a terminal in VS Code with `Terminal` -> `New Terminal`.

Then try:

```bash
ollama --version
```

If that prints a version number, Ollama is installed and ready.

If not, install it with:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## Step 2, pull and try a small model

For this workshop we want fast, lightweight models that still give good results.
Start with:

```bash
ollama pull qwen3:4b
```

The `4b` part means this model has about **4 billion parameters**.
Parameters are the internal numbers the model learned during training.

Very roughly:

- bigger models are often stronger, but slower and heavier
- smaller models are often faster, but may give weaker answers

So `qwen3:1.7b` is a smaller version of the same family:

```bash
ollama pull qwen3:1.7b
```

If you want to discover more models later, browse:

```text
https://ollama.com/search
```

Now try the model directly in the terminal:

```bash
ollama run qwen3:4b
```

Ask it a few questions, for example:

- `Write a two-sentence story about a robot chef.`
- `Explain photosynthesis like I am 15 years old.`
- `Give me three game ideas for a school project.`

You may notice that some models first show extra reasoning text such as `Thinking...` before the final answer.
That is your first glimpse of **thinking mode**.

In simple words, thinking mode means the model spends extra effort on reasoning before it answers.
That can improve difficult tasks, but it can also make responses slower.

For now, just notice it.
Later in the workshop, especially in chapter 3, we will use this idea more deliberately.

When you want to leave the chat, type:

```text
/bye
```

or press `Ctrl+D`.

## Step 3, run the Python script

Before running Python code, make sure you are using the shared workshop virtual environment.

If you are in a terminal, activate it with:

```bash
cd /root/genai-workshop
source .venv/bin/activate
```

After that, your prompt usually shows `(.venv)` at the front.

In VS Code, you can also select the interpreter from the command palette or the interpreter selector, and choose:

```text
/root/genai-workshop/.venv/bin/python
```

Open this file:

[`first-local-llm.py`](/root/genai-workshop/01-first-language-model/first-local-llm.py)

You will see a small TODO:

```python
USER_PROMPT = ""
```

Fill in your own prompt, for example:

```python
USER_PROMPT = "Write a short funny story about a robot who wants to become a baker."
```

Then run:

```bash
cd /root/genai-workshop/01-first-language-model
python3 first-local-llm.py
```

## Step 4, experiment

Now start playing with it:

- change the prompt
- change the system prompt
- switch from `qwen3:4b` to `qwen3:1.7b`
- compare speed and answer quality

Some current Ollama models can also use a **thinking mode**.
That means the model spends more effort on reasoning before giving the final answer.

For now, just remember that this exists.
We will use it more seriously in chapter 3.

You can also return to the terminal version and add `--verbose`:

```bash
ollama run qwen3:4b --verbose
```

That shows extra generation details, including speed, which is useful when comparing models.

## What this teaches you

When this works, you have already learned four important ideas:

- an AI model can run locally, not only in the cloud
- Python code can control that model
- different models trade off speed and quality
- the prompt you write has a big effect on the answer

## Questions to think about

- Which model feels fastest?
- Which model gives the most fun answer?
- How small can a model get before the quality becomes disappointing?
- Is it surprising that this runs locally on your own remote machine?

## Why this chapter matters

This first chapter proves the main idea of the whole workshop:

generative AI is not just something that lives in giant cloud systems, you can also run useful and creative models yourself on a GPU machine with very little code.
