import discord
from lists import games
import random

random_game = random.choice(games)

game_embed = discord.Embed(title="Here is your random game!", description=random_game, color=845883)