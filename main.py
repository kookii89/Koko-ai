
from openai import OpenAI

client = OpenAI()

print("🤖 Hello! I am Koko AI.")
print("I am ready to help you!")

while True:
    user_message = input("You: ")

    if user_message.lower() in ["exit", "quit", "خروج"]:
        print("Koko: Goodbye! 👋")
        break

    response = client.responses.create(
        model="gpt-5",
        input=user_message
    )

    print("Koko:", response.output_text)
