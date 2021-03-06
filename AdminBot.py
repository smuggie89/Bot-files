import subprocess
import os
import discord
from discord.ext import commands
import asyncio
import time
import BotsKey

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
#admin = "438702024918302734" in [role.id for role in client.server.roles]

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
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
    await client.say('Messages deleted')

@client.command(pass_context = True)
async def getbans(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)
    embed = discord.Embed(description = "**%s** has been kicked!"%member.name, color = 0xFF0000)
    return await client.say(embed = embed)

@client.event
async def on_member_join(member):
    server = member.server
    for user in server.members:
        if user.server_permissions.administrator:
            await client.send_message(user, "A new member has joined")
    await client.process_commands(message)

@client.event
async def on_message(message):
        if message.content.upper().startswith('!RESTART CHEF'):
            os.system('taskkill /f /im py.exe /FI "WINDOWTITLE eq Chef"')
            time.sleep(10)
            subprocess.Popen(['py.exe', 'ChefBot.py'], creationflags = subprocess.CREATE_NEW_CONSOLE)
        if message.content.upper().startswith('!RESTART SURVIVOR'):
            os.system('taskkill /f /im py.exe /FI "WINDOWTITLE eq Survivor"')
            time.sleep(10)
            subprocess.Popen(['py.exe', 'SurvivorBot.py'], creationflags = subprocess.CREATE_NEW_CONSOLE)
        if message.content.upper().startswith('!RESTART JOHN'):
            os.system('taskkill /f /im py.exe /FI "WINDOWTITLE eq John"')
            time.sleep(10)
            subprocess.Popen(['py.exe', 'JohnBot.py'], creationflags = subprocess.CREATE_NEW_CONSOLE)
        if message.content.upper().startswith('!RESTART SMUG'):
            os.system('taskkill /f /im py.exe /FI "WINDOWTITLE eq Smug"')
            time.sleep(10)
            subprocess.Popen(['py.exe', 'SmugTestBot.py'], creationflags = subprocess.CREATE_NEW_CONSOLE)

        if message.content.upper().startswith('!HELP'):
             for server in client.servers:
                 for channel in server.channels:
                     if channel.name == 'general':
                        if "438702024918302734" in [role.id for role in message.author.roles]:
                            embed = discord.Embed(title="Commands", description="Ah, so i see you need some help! Let me provide you with some queastions you can ask", color=0x27408B)
                            embed.add_field(name="\u200b \t !getbans", value="\u200b \t gives you a list of banned players", inline=False)
                            await client.send_message(message.author, embed=embed)

        if message.content.upper().startswith('!ADMIN'):
            member = message.author
            User = message.author
            server = member.server
            for user in server.members:
                if user.server_permissions.administrator:
                    await client.send_message(member, "As requested %s, the admin codes you require: \n \t - !admin - Request DM of latest Admin commands (in #general channel only) \n \t - !clear # - Clear messages in channel" % (User.mention))
                else:
                    await client.send_message(message.channel, "You are not authorised to do that")
        await client.process_commands(message)

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
client.run(BotsKey.AB)
