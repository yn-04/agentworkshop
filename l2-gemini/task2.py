import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = """
แยก ingredients ตามหมวดหมู่
Now organize this list:

Ingredients:
- 4 small boneless, skinless chicken breast fillets (about 1.25 pounds total), cut into 1-inch cubes
- 3 garlic cloves, peeled
- 1-inch knob of fresh ginger, roughly chopped
- 3 spring onions, roughly chopped
- 2 tbsp clear honey
- Juice from one orange
- 1 tbsp light soy sauce
- 2 tbsp vegetable oil (+ extra for greasing)
- 20 button mushrooms
- 20 cherry tomatoes
- 2 large red peppers, seeded and cut into 1-inch pieces
- 20 wooden skewers, soaked in water for at least 30 minutes
"""

print(f"Sending prompt: '{prompt}'")
response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=prompt
)
print("\nResponse:")
print(response.text)