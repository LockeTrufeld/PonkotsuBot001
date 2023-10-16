import random


def handle_response(username, message) -> str:
    response = None
    p_message = message.lower()
    words = p_message.split()

    if any([keyword in p_message for keyword in ('tuna', 'salmon', 'guppies', 'gourami', 'betta', 'tilapia')]):
        list = ["Feesh?", "Feesh!", "Feesh feesh.", ":fish:", ":tropical_fish:", ":blowfish:"]
        response = list[random.randint(0,5)]

    # COIN FLIP: FLIP UP TO 20 COINS AT A TIME.
    if words[0] == 'flip':
        
        response = "You flipped: "
        side = ["Heads", "Tails"]
        count = 0
        
        try:
            count = int(words[1]) 
        except: 
            response = response + side[random.randint(0,1)]
            
        if count <= 20:
            while (count > 0):
                response = response + side[random.randint(0,1)]
                count = count - 1
                if count > 0:
                    response = response + ", "
            
        elif count > 20:
            response = (response + side[random.randint(0,1)] + ", " + side[random.randint(0,1)] +\
            ", Tai.. OH NO, THE COINS ARE ROLLING AWAY! THERE'S TOO MANY COINS! AHHHHH! \
            THEY ROLLED UNDER THE REFRIDGERATOR!! ... Well, next time, flip no more than 20.")
     
    # DICE ROLL: ROLL UP TO 5 D6. 
    #elif p_message == 'roll':
        #response = "You rolled: " + str(random.randint(1,6))
    if words[0] == 'roll':
        
        response = "You rolled: "
        count = 0
        total = 0
        
        try:
            count = int(words[1]) 
        except: 
            response = response + str(random.randint(1,6))
            
        if count <= 5:
            while (count > 0):
                die_roll = random.randint(1,6)
                response = response + str(die_roll)
                count = count - 1
                total = total + die_roll
                if count > 0:
                    response = response + ", "
                else:
                    response = response + ".\nTotal: " + str(total)
            
        elif count > 5:
            response = "I only have 5 dice."
            
    # BASIC RESPONSES

    elif any([keyword in p_message for keyword in ('hello', 'hola', 'hallo')]):
        response = "Ya'hallo~"
        
    elif any([keyword in p_message for keyword in('ponkotsu', 'ponkotsubot', 'junk bot')]):
        list = ["Did someone call?", "Huh? What? Sorry, I was feeding the fish.", "Hi, " + username +\
                "! Do you want me to flip a coin?", "I'm listening."]
        response = list[random.randint(0,3)]

    # TODO: !today COMMAND THAT PULLS TODAY'S DATE AND ANY HOLIDAYS IT IS. (FROM WHERE?)

    elif p_message == '!help':
        response = ("`I don't really have a user guide. I just kind of do whatever. Tell me what feature you'd "
                    + "want from me though. Maybe I'll have it eventually.`")
    
    return response