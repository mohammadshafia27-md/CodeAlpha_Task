import random


# Function to generate chatbot replies
def chatbot_reply(user_input):
    user_input = user_input.lower().strip()

    greetings = ["hello", "hi", "hey"]
    goodbyes = ["bye", "goodbye", "see you", "take care"]

    if any(word in user_input for word in greetings):
        return random.choice([
            "Hey there! How are you doing today?",
            "Hi! Nice to see you 😊",
            "Hello! How’s your day going?"
        ])

    elif "how are you" in user_input:
        return random.choice([
            "I’m doing great, thanks for asking! How about you?",
            "Feeling good as always! How are you?",
            "I’m fine, and happy to chat with you 😊"
        ])

    elif "fine" in user_input or "good" in user_input:
        return random.choice([
            "Awesome! Glad to hear that!",
            "That’s great 😄",
            "Nice! Keep smiling!"
        ])

    elif any(word in user_input for word in goodbyes):
        return random.choice([
            "Goodbye! Take care 👋",
            "See you soon! Have a great day!",
            "Bye! It was nice talking to you 😊"
        ])

    else:
        return random.choice([
            "Hmm, I’m not sure I understand. Could you say that differently?",
            "Interesting! Tell me more about that.",
            "Oh, that’s something new to me! 😅"
        ])


# Main chat loop
def main():
    print("Chatbot 🤖: Hi there! I’m your friendly chat buddy. Type 'bye' anytime to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
            print("Chatbot 🤖:", random.choice([
                "Goodbye! Take care 👋",
                "See you later! 😊",
                "Bye! Have a wonderful day!"
            ]))
            break

        response = chatbot_reply(user_input)
        print("Chatbot 🤖:", response)


# Run the chatbot
main()
