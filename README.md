# Barber Shop Booking Agent 💈

A Multi-Agent System designed to act as a concierge for SMB Barber Shops. This project was developed for the **Google Kaggle Agents Intensive Course - Capstone Project** (Enterprise Agents Track).

## 🏆 Project Overview
This agent handles the end-to-end client experience:
-   **Receptionist**: Greets users and routes them based on intent.
-   **Booking**: Manages appointments (checking availability, booking slots) using a Mock Calendar Tool.
-   **Consultation**: Simulates style advice using Gemini Vision (Mock).
-   **Follow-up**: Collects feedback and user-generated content.

## 📂 Repository Structure
```
.
├── src/
│   ├── agents/         # Individual agent logic (Receptionist, Booking, etc.)
│   ├── tools/          # Custom tools (MockCalendar)
│   ├── main.py         # Entry point and orchestrator
│   └── state.py        # Shared agent state definition
├── submission.ipynb    # All-in-one Notebook for Kaggle Submission
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## 🚀 How to Run
1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the Agent**:
    ```bash
    python src/main.py
    ```
3.  **Interact**:
    -   Type "I want to book a haircut" to test the booking flow.
    -   Type "I have a photo" to test the consultation flow.

## 🛠️ Architecture
The system uses a Hub-and-Spoke architecture where a central **Receptionist Agent** routes tasks to specialized agents. All agents share a common state context.

## 📄 License
MIT
