import discord
from chatterbot import ChatBot
from discord.ext import commands
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
from token_2 import token_2

bot = commands.Bot(command_prefix=".", intents=discord.Intents.default())
chatbot = ChatBot("Steve")
client = discord.Client()
trainer = ChatterBotCorpusTrainer(chatbot)
logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

@bot.event
async def on_ready():
    print("Things are maybe working")


@bot.event
async def on_message(message):
       if "chad" in message.content.lower():
            if message.author.bot: return;
            user_input = message.content
            bot_response = chatbot.get_response(user_input)
            await message.channel.send(bot_response)

@bot.event
async def on_connect():
    await bot.change_presence(
        activity=discord.Game(name="Use joinhoney.com/ref/1h0z5sz to make me happy :)"))

bot.run(token_2)
