import json

def load_faq():
    with open("data/faq.json", "r", encoding="utf-8") as file:
        return json.load(file)

FAQ_DATA = load_faq()

def get_bot_response(user_input):
    user_input = user_input.lower()

    for intent in FAQ_DATA.values():
        for keyword in intent["keywords"]:
            if keyword in user_input:
                return intent["answer"]

    return "Sorry, I didn't understand that. Please contact the institute."
