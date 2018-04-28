# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:27:05 2018

@author: Sam
"""

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import BotsKey

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

chat_filter = ["PINEAPPLE", "APPLE", "CHROME"]
bypass_list = []
#admin = has_role.id("438702024918302734")

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Survivor")

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(game=discord.Game(name='Ark Survival Evolved'))

@client.event
async def on_member_join(member):
    User = member
    channel = client.get_channel("437167787962531852")
    await client.send_message(member, "Welcome %s, to Smuggie's Ark. It's dangerous out there, better not go it alone, we are all here to help you survive! \n If its Dino Stats your after head to the #dino channel and type !help for a list of commands where John can help you. \n If its recipe details you need jump onto the #recipe channel and enter the command !help to find out how Chef can help you. Thanks for joining the Ark." % (User.mention))
    await client.send_message(channel, "Welcome %s, to Smuggie's Ark. It's dangerous out there, better not go it alone, we are all here to help you survive!" % (User.mention))

@client.event
async def on_message(message):
    admin = "438702024918302734" in [role.id for role in message.author.roles]
#    contents = message.content.split(" ")
#    for word in contents:
#        if word.upper() in chat_filter:
#            if not message.author.id in bypass_list:
#                try:
#                    await client.delete_message(message)
#                    await client.send_message(message.channel, "**Hey!** You're not allowed to use that word here!")
#                except discord.errors.NotFound:
#                    return

client.run(BotsKey.SB)
