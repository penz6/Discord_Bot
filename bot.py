import logging
import discord
from token import token_1

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


#Poll
@bot.event
@commands.is_owner()
async def on_message(message):
    if "poll" in message.content.lower():
        checkandx = ["<:check:862204980144373790>", "<:nope:862205092161519616>"]
        await add_reaction(checkandx)

@bot.event
async def on_connect():
    await bot.change_presence(
        activity=discord.Game(name="Reworked :)"))


bot.run(token_1)
