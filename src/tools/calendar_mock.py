import datetime
import json
from typing import List, Dict, Optional

class MockCalendarTool:
    """
    A mock implementation of a Calendar tool for the Barber Shop Agent.
    Stores events in an in-memory list.
    """
    def __init__(self):
        self.events = []
        # Seed with some dummy events for today
        today = datetime.date.today()
        self.events.append({
            "id": "evt_1",
            "summary": "Haircut - John Doe",
            "start": f"{today}T10:00:00",
            "end": f"{today}T10:45:00",
            "status": "confirmed"
        })
        self.events.append({
            "id": "evt_2",
            "summary": "Beard Trim - Mike Smith",
            "start": f"{today}T14:00:00",
            "end": f"{today}T14:30:00",
            "status": "confirmed"
        })

    def list_events(self, date_str: str) -> str:
        """
        List events for a specific date (YYYY-MM-DD).
        """
        found_events = [e for e in self.events if e["start"].startswith(date_str)]
        if not found_events:
            return f"No events found for {date_str}."
        
        result = f"Events for {date_str}:\n"
        for evt in found_events:
            result += f"- [{evt['start'].split('T')[1]} - {evt['end'].split('T')[1]}] {evt['summary']} (ID: {evt['id']})\n"
        return result

    def check_availability(self, date_str: str, time_str: str) -> bool:
        """
        Check if a specific slot is free. 
        Simple check: assumes 45 min slots for simplicity in this mock.
        """
        requested_start = f"{date_str}T{time_str}"
        # In a real app, we'd do proper datetime overlap logic.
        # Here we just check exact start time match for simplicity or overlap.
        for evt in self.events:
            if evt["start"] == requested_start:
                return False
        return True

    def create_event(self, summary: str, date_str: str, time_str: str, duration_minutes: int = 45) -> str:
        """
        Create a new event.
        """
        if not self.check_availability(date_str, time_str):
            return f"Error: Slot {date_str} {time_str} is already booked."

        new_id = f"evt_{len(self.events) + 1}"
        # Calculate end time (mock logic)
        start_dt = datetime.datetime.strptime(f"{date_str}T{time_str}", "%Y-%m-%dT%H:%M:%S")
        end_dt = start_dt + datetime.timedelta(minutes=duration_minutes)
        
        new_event = {
            "id": new_id,
            "summary": summary,
            "start": f"{date_str}T{time_str}",
            "end": end_dt.strftime("%Y-%m-%dT%H:%M:%S"),
            "status": "confirmed"
        }
        self.events.append(new_event)
        return f"Success: Booked '{summary}' for {date_str} at {time_str}. (ID: {new_id})"

    def delete_event(self, event_id: str) -> str:
        """
        Cancel an event.
        """
        for i, evt in enumerate(self.events):
            if evt["id"] == event_id:
                removed = self.events.pop(i)
                return f"Success: Cancelled event '{removed['summary']}'."
        return f"Error: Event ID {event_id} not found."
