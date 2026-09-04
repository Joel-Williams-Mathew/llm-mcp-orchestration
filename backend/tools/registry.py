from backend.tools.calculator import calculator
from backend.tools.web_search import web_search


TOOL_REGISTRY = {
    "calculator": calculator,
    "web_search": web_search
}


def execute_tool(tool_name: str, arguments: dict):
    tool = TOOL_REGISTRY.get(tool_name)

    if tool is None:
        return f"Unknown tool: {tool_name}"

    try:
        return tool(**arguments)
    except Exception as e:
        return f"Tool execution failed: {str(e)}"