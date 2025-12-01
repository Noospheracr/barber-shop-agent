import sys
import os

# Add the project root to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.state import AgentState
from src.tools.calendar_mock import MockCalendarTool
from src.agents.receptionist import ReceptionistAgent
from src.agents.booking import BookingAgent
from src.agents.consultation import ConsultationAgent
from src.agents.followup import FollowupAgent

def main():
    # Initialize Tools
    calendar_tool = MockCalendarTool()
    
    # Initialize Agents
    receptionist = ReceptionistAgent()
    booking = BookingAgent(calendar_tool)
    consultation = ConsultationAgent()
    followup = FollowupAgent()
    
    # Initialize State
    state: AgentState = {
        "messages": [],
        "next_agent": "receptionist_agent",
        "client_data": {},
        "current_task": None,
        "error": None
    }
    
    print("--- Barber Shop Agent Started ---")
    print("Type 'quit' to exit.")
    
    # Main Loop
    while True:
        # Get user input if we are at a stopping point (i.e., the last message was from assistant or empty)
        if not state["messages"] or state["messages"][-1]["role"] == "assistant":
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit"]:
                break
            state["messages"].append({"role": "user", "content": user_input})
        
        # Router
        current_agent_name = state["next_agent"]
        
        if current_agent_name == "receptionist_agent":
            state = receptionist.run(state)
        elif current_agent_name == "booking_agent":
            state = booking.run(state)
        elif current_agent_name == "consultation_agent":
            state = consultation.run(state)
        elif current_agent_name == "followup_agent":
            state = followup.run(state)
        else:
            print(f"Error: Unknown agent {current_agent_name}")
            state["next_agent"] = "receptionist_agent"

        # Print Assistant Response
        if state["messages"] and state["messages"][-1]["role"] == "assistant":
            print(f"Agent: {state['messages'][-1]['content']}")

if __name__ == "__main__":
    main()
