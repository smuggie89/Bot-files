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
import BotToken

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

chat_filter = ["PINEAPPLE", "APPLE", "CHROME"]
bypass_list = []
#admin = has_role.id("438702024918302734")

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Survivor")

@client.event
async def on_ready():
    print("Bot is ready")
#Clear message commmand
@client.command(pass_context=True)
async def clear(ctx, amount=100):
        channel = ctx.message.channel
        messages = []
        async for message in client.logs_from(channel, limit=int(amount)+1):
            messages.append(message)
        await client.delete_messages(messages)
        await client.say('Messages deleted')

@client.event
async def on_member_join(member):
    User = member
    channel = client.get_channel("437167787962531852")
    await client.send_message(member, "Welcome %s, to Smuggie's Ark. It's dangerous out there, better not go it alone, we are all here to help you survive! \n If its Dino Stats your after head to the #dino channel and type !help for a list of commands where John can help you. \n If its recipe details you need jump onto the #recipe channel and enter the command !help to find out how Chef can help you. Thanks for joining the Ark." % (User.mention))
    await client.send_message(channel, "Welcome %s, to Smuggie's Ark. It's dangerous out there, better not go it alone, we are all here to help you survive!" % (User.mention))

@client.event
async def on_message(message):
    admin = "438702024918302734" in [role.id for role in message.author.roles]
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!** You're not allowed to use that word here!")
                except discord.errors.NotFound:
                    return

    if message.content.upper().startswith('!CLEAR'):
            if "438702024918302734" in [role.id for role in message.author.roles]:
                tmp = await client.send_message(message.channel, 'Clearing messages...')
                async for msg in client.logs_from(message.channel):
                    await client.delete_message(msg)
            else:
                await client.send_message(message.channel, "You are not authorised to do that")

    if message.content.upper().startswith('!ADMIN'):
        if admin == True:
            member = message.author
            User = message.author
            await client.send_message(member, "As requested %s, the admin codes you require: \n \t - !admin - Request DM of latest Admin commands (in #general channel only) \n \t - !clear # - Clear messages in channel" % (User.mention))
        else:
            await client.send_message(message.channel, "You are not authorised to do that")

client.run(BotToken.SBT)
