from backend.tools.calculator import calculator


TOOL_REGISTRY = {
    "calculator": calculator
}


def execute_tool(tool_name: str, arguments: dict):
    tool = TOOL_REGISTRY.get(tool_name)

    if tool is None:
        return f"Unknown tool: {tool_name}"

    try:
        return tool(**arguments)
    except Exception as e:
        return f"Tool execution failed: {str(e)}"