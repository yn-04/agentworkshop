from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioServerParameters

toolset = MCPToolset(
    connection_params=StdioServerParameters(
        command='npx', 
        args=["-y",   
              "@modelcontextprotocol/server-filesystem",
              "D:\\agentworkshop",
        ],
    )
)

root_agent = LlmAgent(
    name='filesystem_assistant',
    model='gemini-2.0-flash',
    instruction='Help user interact with the local filesystem using available tools.',
    tools=[toolset], 
)