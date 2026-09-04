from mcp.server import MCPServer


mcp = MCPServer("Calculator Server")


@mcp.tool()
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""

    try:
        result = eval(
            expression,
            {"__builtins__": {}}
        )

        return str(result)

    except Exception:
        return "Invalid mathematical expression."


if __name__ == "__main__":
    mcp.run()