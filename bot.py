import discord
from token_2 import token_2
from discord.ext import commands
from discord_slash import SlashCommand

bot = commands.Bot(command_prefix=".", intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)

#startup message
@bot.event
async def on_ready():
    print("Things are maybe working")


#Poll / React
@bot.event
async def on_message(message):
    if message.author.id == 586273007077687316 and "poll" in message.content.lower():
        check1 = '<:check:862204980144373790>'
        nope = '<:nope:862205092161519616>'
        await message.add_reaction(check1)
        await message.add_reaction(nope)

#3 option / abc
@bot.event
async def on_message(message):
    if message.author.id == 586273007077687316 and "abc" in message.content.lower():
        emojia = '🇦'
        emojib = '🇧'
        emojic = '🇨'
        await message.add_reaction(emojia)
        await message.add_reaction(emojib)
        await message.add_reaction(emojic)

#4 option / abcd
@bot.event
async def on_message(message):
    if message.author.id == 586273007077687316 and "abcd" in message.content.lower():
        emojia = '🇦'
        emojib = '🇧'
        emojic = '🇨'
        emojid = '🇩'
        await message.add_reaction(emojia)
        await message.add_reaction(emojib)
        await message.add_reaction(emojic)
        await message.add_reaction(emojid)


#help command
@slash.slash(name="poll",description="This is only really useful to admins")
async def poll(ctx):
    embedpollhelp = discord.Embed(title="Poll Commands", description="Only really useful to admins")
    embedpollhelp.add_field(name="Check and X", value="Have the word poll in you message", inline=False)
    embedpollhelp.add_field(name="3 choices or ABC", value="Have abc in your message", inline=False)
    embedpollhelp.add_field(name="4 choices or ABCD", value="Have abcd in your message", inline=False)
    await ctx.send(embed=embedpollhelp, hidden=True)


#status
@bot.event
async def on_connect():
    await bot.change_presence(
        activity=discord.Game(name="Reworked :)"))


bot.run(token_2)
