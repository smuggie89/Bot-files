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
import BotToken

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

chat_filter = ["PINEAPPLE", "APPLE", "CHROME"]
bypass_list = []

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("John")

@client.event
async def on_ready():
    print("Bot is ready")

@Client.event
async def on_message(message):
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!** You're not allowed to use that word here!")
                except discord.errors.NotFound:
                    return

    if message.content.startswith('!clear'):
            tmp = await client.send_message(message.channel, 'Clearing messages...')
            async for msg in client.logs_from(message.channel):
                await client.delete_message(msg)

client.run(BotToken.JBT)
