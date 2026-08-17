

from tool_registry import TOOLS

TOOLS_SCHEMAS = {
    "get_server_status" : {
        "required": ["system"]
    },
    "create_jira_ticket" : {
        "required" : ["title"]
    }
}

def validate_agent_action(action):
    if not isinstance(action, dict):
        raise ValueError("Agent action must be a dictionary")
    
    action_type = action.get("type")

    if action_type not in ["tool_call", "final_answer"]:
        raise ValueError("Invalid action type")
    
    if action_type == "final_answer":
        if "answer" not in action:
            raise ValueError("Final Answer action must have answer.")
        return True
    
    tool_name = action.get("tool")

    if not tool_name:
        raise ValueError("Missing tool name")
    
    if tool_name not in TOOLS:
        raise ValueError(f"Unkown tool : {tool_name}")
    
    arguments = action.get("arguments", {})

    required_arguments = TOOLS_SCHEMAS.get(
        tool_name,
        {}
    ).get(
        "required", []
    )

    for arg in required_arguments:
        if arg not in arguments:
            raise ValueError(f"Missing required argument '{arg}' for tool '{tool_name}'")
        
    return True


def validate_tool_request(tool_request):
    if not isinstance(tool_request, dict):
        raise ValueError("Tool request must be didctionary")
    
    tool_name = tool_request.get("tool")

    if not tool_name:
        raise ValueError("Missing Tool Name")
    
    if tool_name not in TOOLS:
        raise ValueError(f"{tool_name} is not registered")
    
    arguments = tool_request.get("arguments", {})

    required_arguments = TOOLS_SCHEMAS.get(tool_name, {}).get("required", [])

    for argument in required_arguments:
        if argument not in arguments:
            raise ValueError(f"Missing required argument '{argument}' for tool '{tool_name}")
    
    return True