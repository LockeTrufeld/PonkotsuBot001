import random


def handle_response(message) -> str:
    response = None
    p_message = message.lower()

    if any([keyword in p_message for keyword in ('fish', 'feesh', 'swim', 'fin')]):
        list = ["Feesh?", "Feesh!", "Feesh feesh.", ":fish:", ":tropical_fish:", ":blowfish:"]
        response = list[random.randint(0,5)]

    elif any([keyword in p_message for keyword in ('hello', 'hi', 'hey', 'hallo')]):
        response = "Ya'hallo~"

    elif p_message == 'roll':
        response = "You rolled: " + str(random.randint(1,6))

    elif p_message == '!help':
        response = "`Oh god, what am I doing? What do you want me to do!?`"
    
    return response