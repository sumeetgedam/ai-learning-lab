
from agent import execute_tool
from validator import validate_agent_action
from llm_decision import decide_next_step

from trace_logger import TraceLogger

trace_logger = TraceLogger()

MAX_STEPS = 5

def run_agents(user_query):
    observations = []

    for step in range(MAX_STEPS):
        action = decide_next_step(
            user_query=user_query,
            observations=observations
        )

        trace_logger.log_action(step=step+1, action=action)

        print(f"\nStep {step+1} Actions : ")
        print(action)

        validate_agent_action(action)

        if action["type"] == "final_answer":
            trace_logger.print_trace()
            return action["answer"]
        
        tool_result = execute_tool(action)

        trace_logger.log_observation(tool_result)

        observation = {
            "tool" : action["tool"],
            "result" : tool_result
        }

        observations.append(observation)

        print("\nObservation : ")
        print(observation)
    
    return "Agent stopped because max steps were reached"


if __name__ == "__main__":
    query = input("\nEnter your query : ")

    final_answer = run_agents(query)

    print("\nFinal Answer : \n")
    print(final_answer)