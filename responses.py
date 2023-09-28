import random


def handle_response(message) -> str:
    p_message = message.lower()

    if any([keyword in p_message for keyword in ('fish', 'feesh', 'swim', 'fin')]):
        list = ["Feesh?", "Feesh!", "Feesh feesh.", ":fish:", ":tropical_fish:", ":blowfish:"]
        return list[random.randint(0,5)]

    if any([keyword in p_message for keyword in ('hello', 'hi', 'hey', 'hallo')]):
        return "Ya'hallo~"

    if p_message == 'roll':
        return "You rolled: " + str(random.randint(1,6))

    if p_message == '!help':
        return "`Oh god, what am I doing? What do you want me to do!?`"
    
    