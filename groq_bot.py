from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

history = [{"role": "system", "content": "You are a helpful assistant. Only reply what is asked. No more, No less."}]

print("""
    ==================================================
           Welcome to the CLI AI Chatbot!         
    ==================================================
    Commands:
     /reset - Clear chat history and start fresh
     /exit  - Quit the application
    ==================================================\n""")

while True:
    msg = input("YOU: ")

    if msg == "/exit":
        break
    if msg == "/reset":
        history = [{"role": "system", "content": "You are a helpful assistant. Only reply what is asked. No more, No less."}]
        print("Chat reset.\n")
        continue

    history.append({"role": "user", "content": msg})

    try:
        res = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=history
        )
        reply = res.choices[0].message.content
        print("BOT: ", reply, "\n")
        history.append({"role": "assistant", "content": reply})
    except Exception:
        print("Bot: API error. Please try again.\n")