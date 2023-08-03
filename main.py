import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# English command text
command_text = "Write a Python function to calculate the factorial of a number."

# Preprocess the command text
doc = nlp(command_text)

# Your code for intent recognition and code generation goes here
# ...

# Print the tokens to verify preprocessing (optional)
for token in doc:
    print(token.text, token.pos_)
