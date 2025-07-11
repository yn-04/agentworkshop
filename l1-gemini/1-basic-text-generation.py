import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = "เขียนสโลแกนสั้นๆ เกี่ยวกับai"
print(f"Sending prompt: '{prompt}'")
response = client.models.generate_content(
    model='gemini-2.0-flash-lite', # Fast, cheap model for text generation
    contents=prompt
)
print("\nResponse:")
print(response.text)
print(response)