from tool_registry import TOOLS

def decide_tool(user_query):
    query = user_query.lower()


    if "server" in query and "status" in query:
        return {
            "tool" : "get_server_status",
            "arguments" : {
                "system" : "production"
            }
        }

    if "jira" in query:
        return {
            "tool" : "create_jira_ticket",
            "arguments" : {
                "title" : user_query
            }
        }
    
    return None

def execute_tool(action):
    tool_name = action.get("tool")

    arguments = action.get("arguments", {})

    tool = TOOLS[tool_name]

    if not tool:
        raise ValueError(f"Unknown tool : {tool_name}")

    return tool(**arguments)

