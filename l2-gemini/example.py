import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = """
What's the best method of boiling water?
"""

response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents=prompt,
  config=types.GenerateContentConfig(
  )
)

print("\nResponse:")
print(response.text)
