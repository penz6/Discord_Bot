from chatterbot import ChatBot
import interactions
from token_2 import token_2
from chatterbot.trainers import ChatterBotCorpusTrainer
from interactions import Client, Intents
#imports
bot = interactions.Client(token=token_2,intents=Intents.DEFAULT | Intents.GUILD_MESSAGE_CONTENT)
#bot token
#starts bot
chatbot = ChatBot("Fream")
#trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train(
 #   "chatterbot.corpus.english"
#)
#trains chatbot
@bot.event
async def on_message_create(message):
    if "fream" in message.content.lower():
        if message.author.bot: return;
        user_input = message.content
       #message content to feed to chatbot
        bot_response = chatbot.get_response(user_input)
       #feeds message content to chatbot
        message._client = bot._http
       #http client error hotfix
        bot_response2 = str(bot_response)
        await message.reply(bot_response2)
        
print("started")
bot.start()
