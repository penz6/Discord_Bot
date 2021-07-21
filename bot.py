import discord
from token_2 import token_2
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option

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
        check1 = '<:check:862204980144373790'
        nope = '<:nope:862205092161519616>'
        await message.add_reaction(check1)
        await message.add_reaction(nope)

@slash.slash(name="poll",description="Poll with a check and x",options=[
               create_option(
                 name="pollmessage",
                 description="Put poll content here",
                 option_type=3,
                 required=true
               )
             ])
async def test(ctx, pollmessage: str):
    check1 = '<:check:862204980144373790'
    nope = '<:nope:862205092161519616>'
    await ctx.send(content={pollmessage})
    await message.add_reaction(check1)
    await message.add_reaction(nope)

#help command
@slash.slash(name="poll",description="This is only really useful to admins")
async def poll(ctx):
    embedpollhelp = discord.Embed(title="Poll Commands", description="Only really useful to admins")
    embedpollhelp.add_field(name="Check and X", value="Have the word poll in you message", inline=False)
    await ctx.send(embed=embedpollhelp, hidden=True)


#status
@bot.event
async def on_connect():
    await bot.change_presence(
        activity=discord.Game(name="Reworked :)"))


bot.run(token_2)
