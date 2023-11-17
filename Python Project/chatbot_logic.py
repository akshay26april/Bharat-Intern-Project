# chatbot_logic.py
# Data-driven responses using a dictionary
responses = {
    "how are you?": "I'm doing well, thank you!",
    "what is your name?": "I am your AI chatbot.",
    "how old are you?": "I am an AI, so I don't have an age.",
    # Add more questions and responses here...
}

def get_response(user_input):
    if user_input.lower() in responses:
        return responses[user_input.lower()]
    else:
        return "I'm not sure how to respond to that."

def get_response(user_input):
    # Implement your chatbot's logic here.
    # For simplicity, let's return a fixed response.
    if "hello" in user_input.lower():
        return "Hello! How can I assist you today?"
    elif "help" in user_input.lower():
        return "Sure, I'm here to help. What do you need assistance with?"
    else:
        return "I'm sorry, I couldn't understand your request."

    return "Hello! I am your AI chatbot."
