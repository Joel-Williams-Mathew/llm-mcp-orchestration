import asyncio

from mcp import Client, StdioServerParameters


server = StdioServerParameters(
    command="python",
    args=[
        "mcp_servers/calculator_server/server.py"
    ],
)


async def main():

    async with Client(server) as client:

        print("Connected to MCP server!")

        result = await client.list_tools()

        print("\nAvailable tools:")

        for tool in result.tools:
            print(f"- {tool.name}")

        print("\nCalling calculator...")

        result = await client.call_tool(
            "calculator",
            {
                "expression": "25 * 10"
            }
        )

        print("\nCalculator result:")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())