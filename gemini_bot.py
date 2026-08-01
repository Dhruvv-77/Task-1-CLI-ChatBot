import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

# Load environment variables from .env
load_dotenv()

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not found.")
        print("Please check your .env file.")
        sys.exit(1)

    # Initialize the official Gemini Client
    client = genai.Client(api_key=api_key)
    model_id = "gemini-3.5-flash"

    print("""
    ==================================================
          Welcome to the CLI AI Chatbot!         
    ==================================================
    Commands:
     /reset - Clear chat history and start fresh
     /exit  - Quit the application
    ==================================================\n
""")

    # Initialize multi-turn chat session (maintains context)
    chat = client.chats.create(model=model_id)

    while True:
        try:
            user_input = input("YOU: ").strip()

            if not user_input:
                continue

            # Command handling: Exit
            if user_input.lower() == "/exit":
                print("\nGoodbye!")
                break

            # Command handling: Reset history
            if user_input.lower() == "/reset":
                chat = client.chats.create(model=model_id)
                print("\n---- History cleared. New session started! ----\n")
                continue

            # Send input to model
            print("BOT: ", end="", flush=True)
            response = chat.send_message(user_input)
            print(response.text)
            print()

        except APIError as e:
            print(f"\n[API Error]: {e.message or 'API request failed.'}")
            print("Please try again in a moment.\n")
        except KeyboardInterrupt:
            print("\n\nSession terminated. Goodbye!")
            break
        except Exception as e:
            print(f"\n[Unexpected Error]: {e}\n")

if __name__ == "__main__":
    main()