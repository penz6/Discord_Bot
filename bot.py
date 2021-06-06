import logging
import random
import requests
import discord
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from discord.ext import commands
from discord_slash import SlashCommand
from token_2 import token_2

from lists import games

bot = commands.Bot(command_prefix=".", intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)
chatbot = ChatBot("Steve")
client = discord.Client()
trainer = ChatterBotCorpusTrainer(chatbot)
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)


@bot.event
async def on_ready():
    print("Things are maybe working")


# NPL response
@bot.event
async def on_message(message):
    if "chad" in message.content.lower():
        if message.author.bot: return;
        user_input = message.content
        bot_response = chatbot.get_response(user_input)
        await message.channel.send(bot_response)


# radomizer
@slash.slash(name="select_game", description="Selects a game so you don't have to")
async def _gamepicker(ctx):
    random_game = random.choice(games)
    game_embed = discord.Embed(title="Here is your random game!", description=random_game, color=0x845883)
    await ctx.send(embed=game_embed)


@slash.slash(name="robloxdata", description="Gets the statuses of all our roblox friends :).")
async def _robloxdata(ctx):
    pennonline = requests.get('https://api.roblox.com/users/208564598/onlinestatus/')
    pennonline_json = pennonline.json()
    pennstatus = pennonline_json['IsOnline']
    banonline = requests.get('https://api.roblox.com/users/350444611/onlinestatus/')
    banonline_json = banonline.json()
    banstatus = banonline_json['IsOnline']
    willonline = requests.get('https://api.roblox.com/users/152039976/onlinestatus/')
    willonline_json = willonline.json()
    willstatus = willonline_json['IsOnline']
    henryonline = requests.get('https://api.roblox.com/users/1822340581/onlinestatus/')
    henryonline_json = henryonline.json()
    henrystatus = henryonline_json['IsOnline']
    emilyonline = requests.get('https://api.roblox.com/users/1670729656/onlinestatus/')
    emilyonline_json = emilyonline.json()
    emilystatus = emilyonline_json['IsOnline']
    embedRoblox = discord.Embed(title="Here are statuses you asked for!", color=0x845883)
    embedRoblox.add_field(name="Is Penn online?", value=pennstatus, inline=False)
    embedRoblox.add_field(name="Is Bancroft online?", value=banstatus, inline=False)
    embedRoblox.add_field(name="Is Will online?", value=willstatus, inline=False)
    embedRoblox.add_field(name="Is Henry online?", value=henrystatus, inline=False)
    embedRoblox.add_field(name="Is Emily online?", value=emilystatus, inline=False)
    await ctx.send(embed=embedRoblox)


@bot.event
async def on_connect():
    await bot.change_presence(
        activity=discord.Game(name="Happy pride month! 🏳️‍🌈"))


bot.run(token_2)
