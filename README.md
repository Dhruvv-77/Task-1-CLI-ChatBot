# CLI Chatbot Using Google Gemini API

A lightweight command-line chatbot built in Python using the official Google GenAI SDK.

## Features
- Multi-turn conversation history maintenance
- `/reset` command to clear context
- `/exit` command to close the chatbot
- Environment variable configuration for security

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <YOUR_GITHUB_REPO_URL>
   cd cli-chatbot

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Configure your API key:
   Create a .env file in the root directory:

   Code snippet
   GEMINI_API_KEY=your_gemini_api_key_here
   GROQ_API_KEY=your_groq_api_key_here

6. Run the chatbot:

   ```bash
   python gemini_bot.py
   python groq_bot.py
