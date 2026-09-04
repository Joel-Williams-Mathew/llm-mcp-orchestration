import ollama

from backend.tools.registry import execute_tool


tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The mathematical expression to calculate."
                    }
                },
                "required": ["expression"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the internet for current or unknown information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query."
                    }
                },
                "required": ["query"]
            }
        }
    }
]


def generate_response(message: str) -> str:

    messages = [
        {
            "role": "system",
            "content": "You are OmniAgent. Use the calculator tool whenever mathematical calculation is required."
        },
        {
            "role": "user",
            "content": message
        }
    ]

    # First LLM call
    response = ollama.chat(
    model="qwen3:4b",
    messages=messages,
    tools=tools
)

    print("\n========== RAW LLM RESPONSE ==========")
    print(response)
    print("=======================================\n")

    # Check whether the model requested a tool
    if response.message.tool_calls:

        for tool_call in response.message.tool_calls:

            tool_name = tool_call.function.name
            tool_arguments = tool_call.function.arguments

            result = execute_tool(tool_name, tool_arguments)

                # Add the assistant's tool request
            messages.append(response.message)

                # Add the tool result
            messages.append(
                {
                    "role": "tool",
                    "tool_name": "calculator",
                    "content": result
                }
            )

        # Ask the LLM to produce the final answer
        final_response = ollama.chat(
            model="llama3.2:3b",
            messages=messages,
            tools=tools
        )

        return final_response.message.content

    # Normal response if no tool is needed
    return response.message.content