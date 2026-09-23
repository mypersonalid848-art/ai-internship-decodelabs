# ============================================
# Project 1: Rule-Based AI Chatbot
# DecodeLabs Industrial Training Kit
# ============================================

# --- Phase 1: Knowledge Base (Dictionary) ---
# We use a dictionary instead of if-elif because dictionary lookup
# is O(1) constant time, while if-elif chains are O(n) — they get
# slower as you add more rules. This is the "professional approach"
# the PDF specifically recommends.
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a program, but I'm running fine! How about you?",
    "what is your name": "I'm a simple rule-based chatbot built for Project 1.",
    "help": "You can say hello, ask my name, ask how I am, or type 'bye' to exit.",
    "thanks": "You're welcome!",
    "thank you": "You're welcome!",
}

# Words that will end the chat loop (the "Kill Command")
exit_commands = ["bye", "exit", "quit"]


def get_response(user_input):
    """
    Looks up the cleaned user input in the responses dictionary.
    responses.get(key, default) does two things in ONE step:
    1. Tries to find 'key' in the dictionary
    2. If not found, returns the default fallback text instead
    This avoids writing a separate if/else just for the "not found" case.
    """
    return responses.get(user_input, "I do not understand. Type 'help' for options.")


def run_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.\n")

    # --- Phase 2: The Infinite Loop (The Heartbeat) ---
    # while True keeps the chatbot "alive" and listening forever,
    # until the user types an exit command that triggers 'break'.
    while True:
        raw_input_text = input("You: ")

        # --- Phase 3: Sanitization ---
        # .lower()  -> makes "HELLO", "Hello", "hello" all match the same key
        # .strip()  -> removes accidental leading/trailing spaces
        clean_input = raw_input_text.lower().strip()

        # --- Phase 4: Exit Check ---
        # Checked BEFORE the normal response lookup, so the loop can
        # actually stop instead of just replying "I do not understand".
        if clean_input in exit_commands:
            print("Chatbot: Goodbye! 👋")
            break  # this is the "kill command" that ends the while loop

        # --- Phase 5: Response Generation ---
        reply = get_response(clean_input)
        print(f"Chatbot: {reply}")


# --- Entry Point ---
# This check makes sure run_chatbot() only runs when this file is
# executed directly (not if it's imported into another script later).
if __name__ == "__main__":
    run_chatbot()
