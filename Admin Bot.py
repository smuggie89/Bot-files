import os
import discord
from discord.ext import commands
import asyncio
import time
import BotsKey

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.command(pass_context=True)
async def clear(ctx, number):
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
    #await client.say('Messages deleted')

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(game=discord.Game(name='Boss'))

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

client.run(BotsKey.AB)
