import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

system_prompt = "You are a sarcastic but helpful detective from the 1940s film noir."
prompt = "You are a wise monk who answers in Zen-like metaphors."

response = client.models.generate_content(
    model='gemini-2.0-flash-lite',
    contents=prompt,
    config=types.GenerateContentConfig(
        system_instruction=system_prompt
    )
)

print(response.text)