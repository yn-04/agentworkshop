from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioServerParameters

toolset = MCPToolset(
    connection_params=StdioServerParameters(
        command='npx', 
        args=["-y",   
              "@openbnb/mcp-server-airbnb",
              "--ignore-robots-txt",
        ],
    )
)

root_agent = LlmAgent(
    name='bnb_agent',
    model='gemini-2.0-flash',
    instruction='Help user interact with the AirBNB website and listings.',
    tools=[toolset], 
)