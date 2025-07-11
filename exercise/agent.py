from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioServerParameters

# สร้าง MCPToolset สำหรับ Airbnb server
toolset = MCPToolset(
    connection_params=StdioServerParameters(
        command='npx',
        args=[
            "-y",
            "@openbnb/mcp-server-airbnb",
            "--ignore-robots-txt",  # ตัวเลือกนี้ช่วยให้ bypass robots.txt ได้
        ],
    )
)

# สร้าง root agent ที่ใช้ model Gemini และเชื่อมกับ Airbnb MCP tool
root_agent = LlmAgent(
    name='bnb_agent',
    model='gemini-2.0-flash',
    instruction='Help user interact with the Airbnb website and listings.',
    tools=[toolset],
)
