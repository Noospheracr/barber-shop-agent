from src.state import AgentState
from typing import Dict

class ReceptionistAgent:
    def __init__(self, llm=None):
        self.llm = llm # In a real app, this would be the LLM client
        
    def run(self, state: AgentState) -> AgentState:
        """
        Analyzes the last message and decides where to route the user.
        """
        print("--- Receptionist Agent ---")
        last_message = state["messages"][-1]["content"].lower()
        
        # Simple keyword-based routing for the prototype (to avoid LLM dependency if not configured)
        # In production, this would use an LLM to classify intent.
        
        if "book" in last_message or "schedule" in last_message or "appointment" in last_message:
            state["next_agent"] = "booking_agent"
            state["current_task"] = "booking"
            # We don't add a response here, we let the booking agent take over immediately 
            # OR we can add a transition message.
            # Let's add a transition message for clarity in the log.
            # state["messages"].append({"role": "assistant", "content": "I can help you with that. Let me check our schedule."})
            
        elif "style" in last_message or "look" in last_message or "hair" in last_message or "photo" in last_message:
            state["next_agent"] = "consultation_agent"
            state["current_task"] = "consultation"
            
        elif "feedback" in last_message or "review" in last_message:
            state["next_agent"] = "followup_agent"
            state["current_task"] = "followup"
            
        else:
            # Default response if intent is unclear
            state["next_agent"] = None # Stay here or end
            response = "Welcome to the Barber Shop! I can help you book an appointment, consult on a style, or leave feedback. How can I help you today?"
            state["messages"].append({"role": "assistant", "content": response})
            
        return state
