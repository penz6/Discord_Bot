import discord
from token_2 import token_2
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from discord_slash.utils.manage_commands import create_permission
from discord_slash.model import SlashCommandPermissionType

bot = commands.Bot(command_prefix=".", intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)

#startup message
@bot.event
async def on_ready():
    print("Things are maybe working")


#Slash Poll2
@slash.slash(name="poll",description="Poll with a check and x",default_permission=False,options=[
               create_option(
                 name="pollmessage",
                 description="Put poll content here",
                 option_type=3,
                 required=True
               )
             ])
@slash.permission(guild_id=699702428588703828,
                  permissions=[
                    create_permission(586273007077687316, SlashCommandPermissionType.USER, True)
                  ])
async def poll(ctx, pollmessage: str):
    check1 = '<:check:862204980144373790'
    nope = '<:nope:862205092161519616>'
    message = await ctx.send(content=f"{pollmessage}")
    await message.add_reaction(check1)
    await message.add_reaction(nope)


#status
@bot.event
async def on_connect():
    await bot.change_presence(
        activity=discord.Game(name="Speedrunning legit?"))


bot.run(token_2)
