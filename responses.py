import random


def handle_response(message) -> str:
    response = None
    p_message = message.lower()

    # if any([keyword in p_message for keyword in ('fish', 'feesh', 'swim', 'fin')]):
        # list = ["Feesh?", "Feesh!", "Feesh feesh.", ":fish:", ":tropical_fish:", ":blowfish:"]
        # response = list[random.randint(0,5)]

    if any([keyword in p_message for keyword in ('hello', 'hi', 'hey', 'hallo')]):
        response = "Ya'hallo~"

    elif p_message == 'roll':
        response = "You rolled: " + str(random.randint(1,6))

    elif p_message == 'flip':
        side = ["Heads", "Tails"]
        response = "You flipped: " + side[random.randint(0,1)]

    elif p_message == '!help':
        response = ("`I don't really have a user guide. I just kind of do whatever. Tell me what feature you'd "
                    + "want from me though. Maybe I'll have it eventually.`")
    
    return response