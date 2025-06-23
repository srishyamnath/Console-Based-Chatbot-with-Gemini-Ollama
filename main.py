from chat_session import ChatSession
from gemini_bot import GeminiBot
from ollama_bot import OllamaBot

def choose_bot():
    print("Choose your bot:")
    print("1. Gemini")
    print("2. Ollama (phi3:mini)")
    choice = input("Enter 1 or 2: ").strip()
    if choice == '1':
        api_key = input("Enter your Gemini API Key: ").strip()
        return GeminiBot(api_key)
    elif choice == '2':
        return OllamaBot()
    else:
        print("Invalid choice. Try again.")
        return choose_bot()

def main():
    bot = choose_bot()
    session = ChatSession()
    print("\n🤖 Chatbot is ready! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting... 👋")
            break
        session.add("user", user_input)
        response = bot.get_response(user_input)
        session.add("bot", response)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    main()
