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
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(game=discord.Game(name='Boss'))

@client.command(pass_context=True)
async def clear(ctx, number):
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)
    await client.delete_messages(mgs)
    await client.say('Messages deleted')

@client.command(pass_context = True)
async def getbans(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

#@client.command(pass_context = True)
#async def ban(ctx, *, member : discord.Member = None):
#    if not ctx.message.author.server_permissions.administrator:
#        return
#
#    if not member:
#        return await client.say(ctx.message.author.mention + "Specify a user to ban!")
#    try:
#        await client.ban(member)
#    except Exception as e:
#        if 'Privilege is too low' in str(e):
#            return await client.say(":x: Privilege too low!")
#
#    embed = discord.Embed(description = "**%s** has been banned!"%member.name, color = 0xFF0000)
#    return await client.say(embed = embed)
#
#@client.command(pass_context = True)
#async def kick(ctx, *, member : discord.Member = None):
#    if not ctx.message.author.server_permissions.administrator:
#        return
#
#    if not member:
#        return await client.say(ctx.message.author.mention + "Specify a user to kick!")
#    try:
#        await client.kick(member)
#    except Exception as e:
#        if 'Privilege is too low' in str(e):
#            return await client.say(":x: Privilege too low!")
#
#    embed = discord.Embed(description = "**%s** has been kicked!"%member.name, color = 0xFF0000)
#    return await client.say(embed = embed)
#
#@client.event
#async def on_message(message):
#        if message.content.upper().startswith('!RESTART CHEF'):
#            os.system('taskkill /f /im py.exe /FI "WINDOWTITLE eq Chef"')
#            time.sleep(10)
#            os.system('"Chef Bot.py"')
#        if message.content.upper().startswith('!RESTART SURVIVOR'):
#            os.system('taskkill /f /im py.exe /FI "WINDOWTITLE eq Survivor"')
#            time.sleep(10)
#            os.system('"Survivor Bot.py"')
#        if message.content.upper().startswith('!RESTART JOHN'):
#            os.system('taskkill /f /im py.exe /FI "WINDOWTITLE eq John"')
#            time.sleep(10)
#            os.system('"John Bot.py"')
#        if message.content.upper().startswith('!RESTART SMUG'):
#            os.system('taskkill /f /im py.exe /FI "WINDOWTITLE eq Smug"')
#            time.sleep(10)
##            os.system('"Smug Test Bot.py"')

client.run(BotsKey.AB)
