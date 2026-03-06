# Tool Calling with a Weather Tool

Language models sound smart, but they have a big limitation:
they do not automatically know live information from the outside world.

If you ask a normal model for the weather right now, it cannot measure the sky.
It needs help.

This optional chapter focuses on **one thing only**:

- tool calling

We do **not** add web search here.

The goal is to show one clean pattern:

1. the model reads the user question
2. the model decides it needs a tool
3. your Python code runs the tool
4. the model uses the tool result to answer

That is already enough to teach the main idea.

## What you will build

A small script that lets a local LLM answer weather questions.

The model itself does **not** know the weather.
So it will call a Python tool:

- `get_current_weather(city)`

That tool uses the free Open-Meteo APIs:

- geocoding API, to turn a city name into coordinates
- forecast API, to get the current weather

## Step 1, open the script

Open:

[`weather-tool-calling.py`](/root/genai-workshop/12-tool-calling/weather-tool-calling.py)

## Step 2, look at the weather tool

The tool function is already provided for you.
It makes two normal web requests:

- find the city
- get the weather

So the interesting part of this chapter is **not** the REST API itself.
The interesting part is how the model decides to use the tool.

## Step 3, fix the TODOs

There are two small fixes to make.

### TODO 1, give the model access to the tool

Find:

```python
tools=[]  # TODO
```

Replace it so the model can see the `get_current_weather` tool.

### TODO 2, pass the tool result back into the conversation

After the tool runs, the model still needs to see the result.

Find:

```python
# TODO: append the tool result as a tool message
```

Replace it with a message that contains:

- role `tool`
- the tool name
- the tool result

## Step 4, run the script

```bash
/root/genai-workshop/.venv/bin/python /root/genai-workshop/12-tool-calling/weather-tool-calling.py
```

## What to try

- `Should I bring an umbrella in Ghent today?`
- `What is the weather in Bruges right now?`
- `Is it windy in Antwerp at the moment?`
- `How warm is it in Brussels today?`

## What this teaches you

This chapter is the first real step from “chatbot” to “agent”.
The model is no longer only producing text.
It is also deciding when outside information is needed.

That pattern can be extended to many other tools:

- databases
- calculators
- smart home devices
- calendar APIs
- robots

## Why this chapter matters

This chapter teaches a very important lesson:

LLMs do not need to know everything in advance.
They can decide to use tools, and your code can connect those tools to the outside world.
