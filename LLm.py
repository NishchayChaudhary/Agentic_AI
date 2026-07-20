from openai import OpenAI
import streamlit as st
import os

API_KEY = st.secrets.get("API_KEY", os.getenv("API_KEY"))
BASE_URL = st.secrets.get("BASE_URL", os.getenv("BASE_URL", "https://openrouter.ai/api/v1"))
MODEL_NAME = st.secrets.get("MODEL_NAME", os.getenv("MODEL_NAME", "google/gemma-4-26b-a4b-it:free"))

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
