# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
import responses
#intents = discord.Intents(messages=True, guilds=True)
#intents.reactions = True


# IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client(intents=discord.Intents.all())

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1
        
    activity = discord.Game(name="around. Herp derp", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("PonkotsuBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
    print(message.content)
    
    if message.author == bot.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    if user_message[0] == '?':
        user_message = user_message[1:]
        await send_message(message, user_message, is_private=True)
    else:
        await send_message(message, user_message, is_private=False)

unresponded_counter = 0
@bot.event
async def send_message(message, user_message, is_private):
    global unresponded_counter
    response = responses.handle_response(user_message)
    try:
        await message.author.send(response) if is_private else await message.channel.send(response)
        unresponded_counter = 0
    except Exception as e:
        unresponded_counter += 1
        print(unresponded_counter)
        if unresponded_counter % 50 == 0:
            await message.channel.send('Can we talk about something more interesting instead?')
        print(e)

    # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
    #elif message.content == "hello":
        # SENDS BACK A MESSAGE TO THE CHANNEL.
        #await message.channel.send("Ya'hallo~")

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)