import os
import discord
from discord.ext import commands
import asyncio
import time
import BotsKey

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def wait_until_login():
    await client.change_status(game=discord.Game(name='something goes here'))

@client.event
async def on_message(message):
        if message.content.upper().startswith('!RESTART CHEF'):
            os.system('taskkill /f /im py.exe /FI "WINDOWTITLE eq Chef"')
            time.sleep(10)
            os.system('"Chef Bot.py"')
        if message.content.upper().startswith('!RESTART SURVIVOR'):
            os.system('taskkill /f /im py.exe /FI "WINDOWTITLE eq Survivor"')
            time.sleep(10)
            os.system('"Survivor Bot.py"')
        if message.content.upper().startswith('!RESTART JOHN'):
            os.system('taskkill /f /im py.exe /FI "WINDOWTITLE eq John"')
            time.sleep(10)
            os.system('"John Bot.py"')
        if message.content.upper().startswith('!RESTART SMUG'):
            os.system('taskkill /f /im py.exe /FI "WINDOWTITLE eq Smug"')
            time.sleep(10)
            os.system('"Smug Test Bot.py"')

client.run(BotsKey.ABT)
