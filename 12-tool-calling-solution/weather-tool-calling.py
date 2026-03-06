import json
from urllib.parse import urlencode
from urllib.request import urlopen

import ollama

MODEL_NAME = "qwen3:4b"
USER_PROMPT = "Should I bring an umbrella in Ghent today?"

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Rain showers",
    81: "Heavy rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
}


def clean_model_text(text: str) -> str:
    if "</think>" in text:
        text = text.split("</think>", 1)[1]
    return text.strip()


def get_json(url: str) -> dict:
    with urlopen(url, timeout=20) as response:
        return json.load(response)


def get_current_weather(city: str) -> str:
    """
    Get the current weather for a city.

    Args:
        city: The city name to look up.

    Returns:
        A short JSON string with the city name and current weather.
    """
    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search?" + urlencode(
        {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json",
        }
    )
    geocoding_data = get_json(geocoding_url)
    results = geocoding_data.get("results") or []

    if not results:
        return json.dumps({"error": f"City not found: {city}"})

    place = results[0]

    forecast_url = "https://api.open-meteo.com/v1/forecast?" + urlencode(
        {
            "latitude": place["latitude"],
            "longitude": place["longitude"],
            "current": "temperature_2m,apparent_temperature,weather_code,wind_speed_10m",
            "timezone": "auto",
            "forecast_days": 1,
        }
    )
    forecast_data = get_json(forecast_url)
    current = forecast_data["current"]

    result = {
        "city": place["name"],
        "country": place.get("country", ""),
        "temperature_c": current["temperature_2m"],
        "apparent_temperature_c": current["apparent_temperature"],
        "weather": WEATHER_CODES.get(current["weather_code"], f"WMO code {current['weather_code']}"),
        "wind_kmh": current["wind_speed_10m"],
        "time": current["time"],
    }
    return json.dumps(result)


messages = [{"role": "user", "content": USER_PROMPT}]

first_response = ollama.chat(
    model=MODEL_NAME,
    think=False,
    messages=messages,
    tools=[get_current_weather],
)

messages.append(first_response["message"])

tool_calls = first_response["message"].tool_calls or []
assert tool_calls, "The model did not call a tool."

for tool_call in tool_calls:
    tool_result = get_current_weather(**tool_call.function.arguments)
    messages.append(
        {
            "role": "tool",
            "tool_name": tool_call.function.name,
            "content": tool_result,
        }
    )

final_response = ollama.chat(
    model=MODEL_NAME,
    think=False,
    messages=messages,
)

print()
print(f"Model: {MODEL_NAME}")
print("Tool: get_current_weather(city)")
print()
print("Question:")
print(USER_PROMPT)
print()
print("Answer:")
print(clean_model_text(final_response["message"]["content"]))
