import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import BotsKey

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
#admin = discord.Role.id()

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Smug")

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(game=discord.Game(name='Ark Survival Evolved'))

@client.event
async def wait_until_login():
    await client.change_status(game=discord.Game(name='something goes here'))

@client.event
async def on_member_join(member):
    User = member
    server = member.server
    for user in server.members:
        if user.server_permissions.administrator:
            await client.send_message(user, "%s has joined the Ark" % (User.mention))

#@client.event
#async def on_member_role_update(before,after):
#        User = member
#        channel = client.get_channel("437167787962531852")
#        await client.send_message(member, "Congrats %s, you have been promoted to Admin, this means you have have access to the following restricted commands: \n \t - !admin - Request DM of latest Admin commands (in #general channel only) \n \t - !clear # - Clear messages in channel" % (User.mention))
#        await client.send_message(channel, "Congrats %s, you have been promoted to Admin!" % (User.mention))

client.run(BotsKey.STB)
