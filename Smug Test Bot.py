import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import BotToken

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
#admin = "438702024918302734" in [role.id for role in message.author.roles]
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Smug")

async def on_ready():
    print("Bot is ready")

@client.event
async def wait_until_login():
    await client.change_status(game=discord.Game(name='something goes here'))

#@client.event
#async def on_member_role(roles):
#    User = member
#    channel = client.get_channel("437167787962531852")
#    await client.send_message(member, "Congrats %s, you have been promoted to Admin, this means you have have access to the following restricted commands: \n \t - !admin - Request DM of latest Admin commands (in #general channel only) \n \t - !clear # - Clear messages in channel"" % (User.mention))
#    await client.send_message(channel, "Congrats %s, you have been promoted to Admin!" % (User.mention))

client.run(BotToken.STBT)
