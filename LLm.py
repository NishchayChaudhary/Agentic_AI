from openai import OpenAI
from config import API_KEY, BASE_URL, MODEL_NAME

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def chat(messages: list) -> str:
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"LLM Error: {str(e)}"
