# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:55:31 2018

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

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("John")

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(game=discord.Game(name='Lego Jurassic World'))

@client.event
async def on_message(message):
    #contents = message.content.split(" ")
    #for word in contents:
    #    if word.upper() in chat_filter:
    #        if not message.author.id in bypass_list:
    #            try:
    ##                await client.delete_message(message)
    #                await client.send_message(message.channel, "**Hey!** You're not allowed to use that word here!")
    #            except discord.errors.NotFound:
    #                return
#Help
    if message.content.upper().startswith('!HELP'):
         for server in client.servers:
             for channel in server.channels:
                 if channel.name == 'dinos':
                    embed = discord.Embed(title="Commands for #dino channel", description="Ah, so i see you need some help! Let me provide you with some queastions you can ask", color=0x27408B)
                    await client.send_message(channel, embed=embed)

#    if message.content.startswith('!clear'):
#            tmp = await client.send_message(message.channel, 'Clearing messages...')
#            async for msg in client.logs_from(message.channel):
#                await client.delete_message(msg)

client.run(BotsKey.JB)
