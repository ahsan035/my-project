import spacy

# Load the spaCy language model
nlp = spacy.load('en_core_web_sm')

# Available commands for intent recognition
available_commands = {
    "declare_variable": ["declare", "create", "define"],
    "for_loop": ["create a for loop", "make a for loop", "generate a for loop"],
    "print_statement": ["print", "display", "show"]
}

def recognize_intent(command):
    # Process the command using spaCy
    doc = nlp(command)

    # Get the lemmatized version of each token in the command
    lemmatized_tokens = [token.lemma_ for token in doc]

    # Check if any of the available commands' keywords are present in the lemmatized tokens
    for intent, keywords in available_commands.items():
        if any(keyword in lemmatized_tokens for keyword in keywords):
            return intent

    # If no intent is recognized, return "Unrecognized command"
    return "Unrecognized command."

if __name__ == "__main__":
    print("Available commands:")
    for command in available_commands.values():
        print(f"- {command[0]}")

    while True:
        user_input = input("Enter a command (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break

        recognized_intent = recognize_intent(user_input)
        print(f"Recognized intent: {recognized_intent}")
