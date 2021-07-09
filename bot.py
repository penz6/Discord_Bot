import discord
from token_2 import token_2
from discord.ext import commands

bot = commands.Bot(command_prefix=".", intents=discord.Intents.default())
check = "<:check:862204980144373790>"
nope = "<:nope:862205092161519616>"
@bot.event
async def on_ready():
    print("Things are maybe working")


#Poll
@bot.event
async def on_message(message):
    if message.author.id == 586273007077687316 and "poll" in message.content.lower():
        check1 = '<:check:862204980144373790'
        nope = '<:nope:862205092161519616>'
        await message.add_reaction(check1)
        await message.add_reaction(nope)

@bot.event
async def on_connect():
    await bot.change_presence(
        activity=discord.Game(name="Reworked :)"))


bot.run(token_2)
