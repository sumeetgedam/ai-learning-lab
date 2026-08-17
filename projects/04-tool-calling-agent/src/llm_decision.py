import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client  = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def clean_json_response(response_text):

    return (
        response_text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )
    


SYSTEM_PROMPT = """
You are an agent planner.

You can either call a tool or return a final answer.

Available tools :

1. get_server_status
Arguments:
{
    "system":"production"
}

2. create_jira_ticket
Arguments:
{
    "title":"",
    "description":""
}

Return ONLY valid JSON.

If you need to call a tool, return : 

{
    "type" : "tool_call",
    "tool" : "tool_name",
    "arguments" : {}
}

If you have enough information to answer, return : 

{
    "type" : "final_answer",
    "answer" : "....."
}

Rules : 
- If the user asks to create a ticket only if server is down, first call get_server_status.
- If server status is DOWN, call create_jira_ticket.
- If server status is UP, do not create a ticket.
- Never invent a tool.
- Use Observations provided to decide next step.
"""

def decide_next_step(user_query, observations):
    prompt = f"""
{SYSTEM_PROMPT}

User request :
{user_query}

Observations so far :
{observations}
"""
    
    response  = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    cleaned = clean_json_response(response.text)

    return json.loads(cleaned)



def decide_tool_with_llm(query):

    prompt = f"""
{SYSTEM_PROMPT}

User query:
{query}
"""
    
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    # print(response)
    response_text = clean_json_response(response.text)

    return response_text


def generate_final_response(user_query, observations):
    
    prompt = f"""
User Request : 
{user_query}

Observations : 
{observations}

Provide a concise user-friendly final answer.
"""
    
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )
    # print(response)
    return response.text