import logging
import random

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

#NPL response
@bot.event
async def on_message(message):
       if "chad" in message.content.lower():
            if message.author.bot: return;
            user_input = message.content
            bot_response = chatbot.get_response(user_input)
            await message.channel.send(bot_response)

#radomizer
@slash.slash(name="select_game", description="Selects a game so you don't have to")
async def _gamepicker(ctx):
    random_game = random.choice(games)
    game_embed = discord.Embed(title="Here is your random game!", description=random_game, color=0x845883)
    await ctx.send(embed=game_embed)

@bot.event
async def on_connect():
    await bot.change_presence(
        activity=discord.Game(name="Use joinhoney.com/ref/1h0z5sz to make me happy :)"))

bot.run(token_2)
