from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

# Connect to the toolbox server
toolbox = ToolboxSyncClient("http://127.0.0.1:5000")

# Load the available tools
tools = toolbox.load_toolset('basic-toolset')

# Define the agent prompt
prompt = """
You are a helpful university student assistant. 
You handle course searching using tools provided by the university's course management system.
Answer user questions about courses.
Do not answer questions about other topics.
"""

# Create the root agent
root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='course_agent',
    description='A helpful AI assistant.',
    instruction=prompt,
    tools=tools,
)
