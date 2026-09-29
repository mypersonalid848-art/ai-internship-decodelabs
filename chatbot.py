import time

# Knowledge base — 8 intents
data = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a program, but I'm running fine! How about you?",
    "what is your name": "I'm a simple rule-based chatbot built for Project 1.",
    "help": "You can say hello, ask my name, ask how I am, or type 'bye' to exit.",
    "thanks": "You're welcome!",
    "thank you": "You're welcome!",
    "bye": "Goodbye! Have a nice day!",
}

exit_words = ["bye", "exit", "quit"]  # exit/quit এখন থেকে কাজ করবে

while True:
    user_input = input("Enter a query: ").strip().lower()

    if user_input in exit_words:
        print("Thinking....")
        time.sleep(1)
        print(data.get(user_input, "Goodbye!"))
        break

    print("Thinking....")
    time.sleep(1)
    print(data.get(user_input, "I am sorry, I don't understand that."))
