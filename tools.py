import math, datetime, random, requests
from zoneinfo import ZoneInfo
from ddgs import DDGS

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

CITY_TIMEZONES = {
    "delhi": "Asia/Kolkata", "mumbai": "Asia/Kolkata", "gurugram": "Asia/Kolkata",
    "bangalore": "Asia/Kolkata", "kolkata": "Asia/Kolkata", "chennai": "Asia/Kolkata",
    "hyderabad": "Asia/Kolkata", "pune": "Asia/Kolkata", "india": "Asia/Kolkata",
    "new york": "America/New_York", "london": "Europe/London", "paris": "Europe/Paris",
    "tokyo": "Asia/Tokyo", "dubai": "Asia/Dubai", "singapore": "Asia/Singapore",
    "sydney": "Australia/Sydney", "los angeles": "America/Los_Angeles",
    "berlin": "Europe/Berlin", "moscow": "Europe/Moscow", "beijing": "Asia/Shanghai",
}

def get_current_time(city: str) -> str:
    city_key = city.strip().lower() if city else "delhi"
    tz_name = CITY_TIMEZONES.get(city_key, "Asia/Kolkata")
    now = datetime.datetime.now(ZoneInfo(tz_name))
    return f"Current time in {city or 'Delhi'}: {now.strftime('%I:%M %p')} | Date: {now.strftime('%d %B %Y')} ({tz_name})"

def get_joke(category: str = "general") -> str:
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the AI go to school? To improve its learning rate!",
        "How many programmers does it take to change a light bulb? None — it's a hardware problem!",
        "Why did the neural network break up? Too many layers between them!",
        "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads.",
    ]
    return random.choice(jokes)

def web_search(query: str) -> str:
    try:
        results = DDGS().text(query, max_results=3)
        if not results:
            return f"No results found for '{query}'"
        formatted = []
        for r in results:
            formatted.append(f"- {r['title']}: {r['body'][:150]}... ({r['href']})")
        return "\n".join(formatted)
    except Exception as e:
        return f"Web search error: {e}"

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
    elif tool == "search":
        return web_search(tool_request.get("query", ""))
    else:
        return f"Unknown tool: {tool}"
