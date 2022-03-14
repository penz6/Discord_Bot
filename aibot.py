from chatterbot import ChatBot
import interactions
#from token_2 import token_2
from chatterbot.trainers import ChatterBotCorpusTrainer
#imports
bot = interactions.Client(token="TEST")
#bot token
bot.start()
#starts bot
chatbot = ChatBot("Fream")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "chatterbot.corpus.english"
)
#trains chatbot

@bot.event
async def on_message_create(message):
    if "fream" in message.content.lower():
         user_input = message.content
         bot_response = chatbot.get_response(user_input)
         await message.channel.send(bot_response)
        

bot.start()

