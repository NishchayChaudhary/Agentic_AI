import math, datetime, random, requests

def calculator(expression: str) -> str:
    try:
        allowed = {k: v for k, v in math.__dict__.items() if not k.startswith("_")}
        result = eval(expression, {"__builtins__": {}}, allowed)
        return f"{expression} = {result}"
    except Exception as e:
        return f"Calculator error: {e}"

def get_weather(city: str) -> str:
    try:
        url = f"https://wttr.in/{city}?format=3"
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return r.text.strip()
        return f"Could not fetch weather for {city}"
    except:
        return f"Weather service unavailable for {city}"

def get_current_time(city: str) -> str:
    now = datetime.datetime.now()
    return f"Current time: {now.strftime('%I:%M %p')} | Date: {now.strftime('%d %B %Y')} (Local time, city: {city})"

def get_joke(category: str = "general") -> str:
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the AI go to school? To improve its learning rate!",
        "How many programmers does it take to change a light bulb? None — it's a hardware problem!",
        "Why did the neural network break up? Too many layers between them!",
        "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads.",
    ]
    return random.choice(jokes)

def run_tool(tool_request: dict) -> str:
    tool = tool_request.get("tool")
    if tool == "calculator":
        return calculator(tool_request.get("expression", ""))
    elif tool == "weather":
        return get_weather(tool_request.get("city", "Delhi"))
    elif tool == "time":
        return get_current_time(tool_request.get("city", ""))
    elif tool == "joke":
        return get_joke(tool_request.get("category", "general"))
    else:
        return f"Unknown tool: {tool}"
