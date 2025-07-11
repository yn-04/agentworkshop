from google.adk.agents import Agent

prompt = """Jungkook in an edgy streetwear look, neon lights glowing behind him.
Dark city vibes, confident stare, tattooed hand holding a mic.
Cool, cinematic, K-pop rebel energy."""

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    description='A helpful assistant for questions about kpop.',
    instruction=prompt
)