from typing import TypedDict, List, Optional, Dict, Any, Annotated
import operator

class AgentState(TypedDict):
    """
    The shared state of the agent system.
    """
    messages: List[Dict[str, str]] # Chat history: [{"role": "user", "content": "..."}, ...]
    next_agent: Optional[str]      # The next agent to route to
    client_data: Dict[str, Any]    # Data about the client (name, preferences, etc.)
    current_task: Optional[str]    # What the user is currently trying to do (e.g., "booking", "consultation")
    error: Optional[str]           # Any error messages to report
