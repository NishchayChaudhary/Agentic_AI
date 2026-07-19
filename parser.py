import json, re

def parse_tool_call(text: str):
    try:
        text = text.strip()
        match = re.search(r'\{.*?\}', text, re.DOTALL)
        if match:
            obj = json.loads(match.group())
            if "tool" in obj:
                return obj
    except:
        pass
    return None
