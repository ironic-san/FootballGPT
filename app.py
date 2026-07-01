from chatbot import FootballChatbot

bot = FootballChatbot()

print("=" * 50)
print("⚽ Welcome to FootballGPT")
print("Type 'exit', 'quit' or 'bye' to quit.")
print("=" * 50)

while True:

    user = input("\nYou: ")

    if user.lower() in ["exit", "quit", "bye"]:
        print("\n👋 Goodbye!")
        break

    answer = bot.chat(user)

    print("\nFootballGPT:")
    print(answer)