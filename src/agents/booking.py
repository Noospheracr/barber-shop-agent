from src.state import AgentState
from src.tools.calendar_mock import MockCalendarTool
import datetime

class BookingAgent:
    def __init__(self, calendar_tool: MockCalendarTool):
        self.calendar = calendar_tool

    def run(self, state: AgentState) -> AgentState:
        print("--- Booking Agent ---")
        last_message = state["messages"][-1]["content"]
        
        # Very simple state machine for booking
        # 1. Ask for date/time if not present
        # 2. Check availability
        # 3. Book
        
        # Check if we have a pending booking request in client_data or if we need to parse it
        # For this prototype, we'll do a simple multi-turn logic based on keywords.
        
        today = datetime.date.today().isoformat()
        
        # Mock parsing logic (replace with LLM extraction in real app)
        # If user says a time, try to book.
        if " at " in last_message or ":" in last_message:
            # Assume user provided a time, e.g., "at 10:00"
            # We'll just try to parse a simple time string for the demo
            try:
                # Extract time (very naive)
                words = last_message.split()
                time_str = "10:00:00" # Default fallback
                for w in words:
                    if ":" in w:
                        time_str = w
                        if len(time_str) == 5: # HH:MM
                            time_str += ":00"
                        break
                
                date_str = today # Assume today for simplicity
                
                result = self.calendar.create_event("Client Appointment", date_str, time_str)
                state["messages"].append({"role": "assistant", "content": result})
                state["next_agent"] = "receptionist_agent" # Return to main menu
                state["current_task"] = None
                
            except Exception as e:
                state["messages"].append({"role": "assistant", "content": f"I had trouble booking that. Please specify time in HH:MM format. (Error: {str(e)})"})
                
        else:
            # Show availability
            events = self.calendar.list_events(today)
            response = f"Here is the schedule for today ({today}):\n{events}\nWhat time would you like to come in? (e.g., 'at 10:00')"
            state["messages"].append({"role": "assistant", "content": response})
            # Stay in booking agent
            state["next_agent"] = "booking_agent"
            
        return state
