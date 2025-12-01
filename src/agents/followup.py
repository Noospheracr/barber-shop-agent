from src.state import AgentState

class FollowupAgent:
    def __init__(self):
        pass

    def run(self, state: AgentState) -> AgentState:
        print("--- Follow-up Agent ---")
        last_message = state["messages"][-1]["content"].lower()
        
        if "good" in last_message or "great" in last_message or "bad" in last_message:
            response = "Thank you for your feedback! We'd love to see your fresh cut. Would you mind sharing a selfie for our social media? (We'll offer a discount on your next visit!)"
            state["messages"].append({"role": "assistant", "content": response})
            state["next_agent"] = "followup_agent"
            
        elif "sure" in last_message or "okay" in last_message or "yes" in last_message:
             response = "Awesome! Please upload it whenever you're ready. See you next time!"
             state["messages"].append({"role": "assistant", "content": response})
             state["next_agent"] = "receptionist_agent" # Done
             
        else:
            response = "How was your last visit? We value your feedback."
            state["messages"].append({"role": "assistant", "content": response})
            state["next_agent"] = "followup_agent"
            
        return state
