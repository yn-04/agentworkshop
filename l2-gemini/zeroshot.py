import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = """
Q: The cafeteria had 23 apples.
If they used 20 to make lunch and bought 6 more, how many apples do they have?
A: Let's think step by step.
"""

print(f"Sending prompt: '{prompt}'")
response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=prompt
)
print("\nResponse:")
print(response.text)