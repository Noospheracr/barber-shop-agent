from src.state import AgentState
import time

class ConsultationAgent:
    def __init__(self):
        pass

    def run(self, state: AgentState) -> AgentState:
        print("--- Consultation Agent ---")
        last_message = state["messages"][-1]["content"].lower()
        
        if "photo" in last_message or "image" in last_message or "upload" in last_message:
            # Simulate analyzing an image
            # In a real app, we would check for image attachment in the message
            response = "I see you've shared a photo (simulated). Analyzing style..."
            state["messages"].append({"role": "assistant", "content": response})
            
            # Mock Gemini Vision analysis
            analysis = "This looks like a 'Textured Crop' with a high fade. It suits your face shape well."
            state["messages"].append({"role": "assistant", "content": f"Gemini Vision Analysis: {analysis}\nWould you like to book this style?"})
            
            # Update client preferences
            state["client_data"]["preferred_style"] = "Textured Crop"
            
        elif "yes" in last_message and state["client_data"].get("preferred_style"):
             state["next_agent"] = "booking_agent"
             state["messages"].append({"role": "assistant", "content": "Great! Let's get you booked for that."})
             
        else:
            response = "I can help you choose a style. You can upload a photo of a look you like, or describe it to me."
            state["messages"].append({"role": "assistant", "content": response})
            state["next_agent"] = "consultation_agent" # Stay here
            
        return state
