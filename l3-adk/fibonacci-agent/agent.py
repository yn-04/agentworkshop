from google.adk.agents import Agent
 
prompt = """Answer questions about the Fibonacci sequence. Use the tool to compute the nth Fibonacci number."""
 
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number starting from 0, 1."""
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
 
root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    description='A helpful assistant for math problems, including Fibonacci sequence calculations.',
    instruction=prompt,
    tools=[fibonacci]
)