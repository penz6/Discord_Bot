import discord
from token_2 import token_2
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from discord_slash.utils.manage_commands import create_permission
from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle


bot = commands.Bot(command_prefix=".", intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)

#startup message
@bot.event
async def on_ready():
    print("Things are maybe working")

#announcement button
@bot.event
async def on_component(ctx: announcementbutton, custom_id=announcement):
  announcementrole = ctx.guild.get_role(739529929955213482)
  await user.add_roles(announcementrole)

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

#mute command
@slash.slash(name="mute",description="Mute people",default_permission=False,options=[
               create_option(
                 name="user",
                 description="The user you want to mute",
                 option_type=6,
                 required=True
               )
             ])
@slash.permission(guild_id=699702428588703828,
                  permissions=[
                    create_permission(717869653946531962, SlashCommandPermissionType.ROLE, True)
                  ])
async def mute(ctx, user: discord.Member):
    muterole = ctx.guild.get_role(710621437043540041)
    await user.add_roles(muterole)
    await ctx.send(content="Success!")

#unmute command
@slash.slash(name="unmute",description="Unmute people",default_permission=False,options=[
               create_option(
                 name="user",
                 description="The user you want to unmute",
                 option_type=6,
                 required=True
               )
             ])
@slash.permission(guild_id=699702428588703828,
                  permissions=[
                    create_permission(717869653946531962, SlashCommandPermissionType.ROLE, True)
                  ])
async def mute(ctx, user: discord.Member):
    muterole = ctx.guild.get_role(710621437043540041)
    await user.remove_roles(muterole)
    await ctx.send(content="Success!")

#react role
@slash.slash(name="createannouncerole",description="Create a react message for the announcement role",default_permission=False)
@slash.permission(guild_id=699702428588703828,
                  permissions=[
                    create_permission(717869653946531962, SlashCommandPermissionType.ROLE, True)
                  ])
async def reactrol(ctx):
  await ctx.send(content="Click the button to be informed when we annonce things!", components=[
                                    create_actionrow(
                                        create_button(style=ButtonStyle.green, label="Announcement Role!", custom_id=announcement))
                                    ])


#status
@bot.event
async def on_connect():
    await bot.change_presence(
        activity=discord.Game(name="Speedrunning legit no cheats!?"))


bot.run(token_2)
