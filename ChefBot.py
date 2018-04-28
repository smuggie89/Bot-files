# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:21:05 2018

@author: Sam
"""

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import BotsKey
import Functions

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

chat_filter = ["PINEAPPLE", "APPLE", "CHROME"]
bypass_list = []

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Chef")

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(game=discord.Game(name='With his Chocolate Salty Balls'))

@client.event
async def on_message(message):
    def e_w_k_f(kibblename, kibblenumber):
        if message.content.upper().endswith(kibblename) or message.content.upper().endswith(kibblenumber):
            return True

    def em_k_f(eggname, eggrecipe, eggtaming):
           embed = discord.Embed(title= (eggname) + " Egg", description="This recipe is used to make Kibble (" + (eggname) + " Egg)", color=0x00ff00)
           embed.add_field(name="Ingredients", value= (eggrecipe), inline=False)
           embed.add_field(name="Dino Taming", value= (eggtaming), inline=False)
           return embed

    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!** You're not allowed to use that word here!")
                except discord.errors.NotFound:
                    return

    if message.content == "!cookie":
        await client.send_message(message.channel, ":cookie:")

    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!SAY'):
        if message.author.id == "433043997414522891":
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You do not have permission")
    if message.content.upper().startswith('!AMIADMIN'):
        if "438702024918302734" in [role.id for role in message.author.roles]:
           await client.send_message(message.channel, "You are an admin")
        else:
            await client.send_message(message.channel, "You are not an admin")
#Help
    if message.content.upper().startswith('!HELP'):
            embed = discord.Embed(title="Commands for #recipe channel", description="Ah, so i see you need some help! Let me provide you with some queastions you can ask", color=0x27408B)
            embed.add_field(name="\u200b \t !kibble", value="\u200b \t gives you a list of all available kibble recipes", inline=False)
            embed.add_field(name="\u200b \t !kibble <kibble name>", value="\u200b \t provides recipe and details of sepcified kibble", inline=False)
            embed.add_field(name="\u200b \t !food", value="\u200b \t gives a list of all available food recipes", inline=False)
            embed.add_field(name="\u200b \t !food <food name>", value="\u200b \t provides details of specified food", inline=False)
            #embed.add_field(name=" ", value="\t !kibble - gives you a list of all available kibble recipes \n \t !kibble <kibble name> - provides recipe and details of sepcified kibble \n \t !food - gives a list of all available food recipes \n \t !food <food name> - provides details of specified food", inline=False)
            await client.send_message(message.channel, embed=embed)
#Kibble Recipes
    if message.content.upper().startswith('!KIBBLE'):
        if e_w_k_f('ALLOSAURUS EGG', '1'):
            await client.send_message(message.channel, embed=em_k_f("Allosaurus", "\u200b \t 1x Allosaurus Egg \n \t 1x Savoroot \n \t 1x Cooked Prime Meat \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Tapejare, Griffin"))
        elif e_w_k_f('ANKYLO EGG', '2'):
            await client.send_message(message.channel, embed=em_k_f("Ankylo", "\u200b \t 1x Ankylo Egg \n \t 1x Savoroot \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Carno"))
        elif e_w_k_f('ARANEO EGG', '3'):
            await client.send_message(message.channel, embed=em_k_f("Araneo", "\u200b \t 1x Araneo Egg \n \t 1x Rockarrot \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "\u200b"))
        elif e_w_k_f('ARCHAEOPTERYX EGG', '4'):
             await client.send_message(message.channel, embed=em_k_f("Archaeopteryx", "\u200b \t 1x Archaeopteryx Egg \n \t 1x Longrass \n \t 1x Cooked Fish Meat \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Diplocaulus"))
        elif e_w_k_f('ARGENTAVIS EGG', '5'):
            await client.send_message(message.channel, embed=em_k_f("Argentavis", "\u200b \t 1x Argentavis Egg \n \t 1x Citronal \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin","Spino"))
        elif e_w_k_f('BARYONYX EGG', '6'):
            await client.send_message(message.channel, embed=em_k_f("Baryonyx", "\u200b \t 1x Baryonyx Egg \n \t 1x Savoroot \n \t 1x Raw Mutton \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Megalania"))
        elif e_w_k_f('BRONTO EGG', '7'):
            await client.send_message(message.channel, embed=em_k_f("Bronto", "\u200b \t 1x Bronto Egg \n \t 1x Rockarrot \n \t 1x Cooked Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Sabertooth"))
        elif e_w_k_f('CARNO EGG', '8'):
            await client.send_message(message.channel, embed=em_k_f("Carno", "\u200b \t 1x Carno Egg \n \t 1x Savoroot \n \t 1x Cooked Meat \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Trike, Direwolf, Direbear"))
        elif e_w_k_f('COMPY EGG', '9'):
            await client.send_message(message.channel, embed=em_k_f("Compy", "\u200b \t 1x Compy Egg \n \t 1x Citronal \n \t 1x Cooked Fish Meat \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Kentrosaurus"))
        elif message.content.upper().endswith('DILO EGG') or message.content.upper().endswith('10'):
            embed = discord.Embed(title="Dilo Egg", description="This recipe is used to make Kibble (Dilo egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Dilo Egg \n \t 1x Citronal \n \t 1x Cooked Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Ankylo, Doedicurus, Pachy", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('DIMETRODON EGG') or message.content.upper().endswith('11'):
            embed = discord.Embed(title="Dimetrodon Egg", description="This recipe is used to make Kibble (Dimetrodon egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Dimetrodon Egg \n \t 1x Citronal \n \t 1x Cooked Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Gallimimus", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('DIMORPH EGG') or message.content.upper().endswith('12'):
            embed = discord.Embed(title="Dimorph Egg", description="This recipe is used to make Kibble (Dimorph egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Dimorph Egg \n \t 1x Longrass \n \t 1x Cooked Meat or Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Megaloceros", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('DIPLO EGG') or message.content.upper().endswith('13'):
            embed = discord.Embed(title="Diplo Egg", description="This recipe is used to make Kibble (Diplo Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Diplo Egg \n \t 1x Savoroot \n \t 1x Rare Flower \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Allosaurus", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('DODO EGG') or message.content.upper().endswith('14'):
            embed = discord.Embed(title="Dodo Egg", description="This recipee is used to make Kibble (Dodo egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Dodo Egg \n \t 1x Rockarrot \n \t 1x Cooked Meat or Cooked Fish Meat \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Pteranodon, Ichthy, Mesopithecus", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('FEATHERLIGHT EGG') or message.content.upper().endswith('15'):
            embed = discord.Embed(title="FeatherLight Egg", description="This recipee is used to make Kibble (Featherlight egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Featherlight Egg \n \t 3x Auric Mushroom \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="\u200b", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('GALLIMIMUS EGG') or message.content.upper().endswith('16'):
            embed = discord.Embed(title="Gallimimus Egg", description="This recipe is used to make Kibble (Gallimimus egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Gallimimus Egg \n \t 1x Savoroot \n \t 1x Cooked Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Terror Bird, Castoroides", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('GLOWTAIL EGG') or message.content.upper().endswith('17'):
            embed = discord.Embed(title="Glowtail Egg", description="This recipe is used to make Kibble (Glowtail egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Glowtail Egg \n \t 3x Aquatic Mushroom \n \t 1x Cooked Fish Meat \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="\u200b", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('ICHTHYORNIS EGG') or message.content.upper().endswith('18'):
            embed = discord.Embed(title="Ichthyornis Egg", description="This recipe is used to make Kibble (Ichthyornis Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Ichthyornis Egg \n \t 1x Savoroot \n \t 1x Rare Flower \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Giant Bee", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('IGUANODON EGG') or message.content.upper().endswith('19'):
            embed = discord.Embed(title="Iguanodon Egg", description="This recipe is used to make Kibble (Iguanodon Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Iguanodon Egg \n \t 1x Rare Mushroom \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Daeodon", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('KAIRUKU EGG') or message.content.upper().endswith('20'):
            embed = discord.Embed(title="Kairuku Egg", description="This recipe is used to make Kibble (Kairuku Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Kairuku Egg \n \t 1x Savoroot \n \t 1x Cooked Meat or Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Angler", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('KAPROSUCHUS EGG') or message.content.upper().endswith('21'):
            embed = discord.Embed(title="Kaprosuchus Egg", description="This recipe is used to make Kibble (Kaprosuchus Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Kaprosuchus Egg \n \t 1x Savoroot \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="\u200b", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('KENTRO EGG') or message.content.upper().endswith('22'):
            embed = discord.Embed(title="Kentro Egg", description="This recipe is used to make Kibble (Kentro Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Kentro Egg \n \t 1x Amonite Bile \n \t 1x Golden Hesperornis Egg \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Yutyrannus", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('LYSTROSAURUS EGG') or message.content.upper().endswith('23'):
            embed = discord.Embed(title="Lystrosaurus Egg", description="This recipe is used to make Kibble (Lystrosaurus egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Lystrosaurus Egg \n \t 1x Rockarrot \n \t 1x Cooked Prime Meat or Prime Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Diplodocus", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('MANTIS EGG') or message.content.upper().endswith('24'):
            embed = discord.Embed(title="Mantis Egg", description="This recipe is used to make Kibble (Mantis egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Mantis Egg \n \t 1x Citronal \n \t 1x Obsidian \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Rock Elemental", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('MEGALANIA EGG') or message.content.upper().endswith('25'):
            embed = discord.Embed(title="Megalania Egg", description="This recipe is used to make Kibble (Megalania Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Megalania Egg \n \t 1x Giant Bee Honey \n \t 10x Chitin \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Megatherium", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('MEGALOSAURUS EGG') or message.content.upper().endswith('26'):
            embed = discord.Embed(title="Megalosaurus Egg", description="This recipe is used to make Kibble (Megalosaurus Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Megalosaurus Egg \n \t 1x Rockarrot \n \t 2x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Therizinosaurus", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('MICRORAPTOR EGG') or message.content.upper().endswith('27'):
            embed = discord.Embed(title="Microraptor Egg", description="This Recipe is used to make Kibble (Microraptor Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Microraptor Egg \n \t 1x Longrass \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Iguanodon", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('MORELLATOPS EGG') or message.content.upper().endswith('28'):
            embed = discord.Embed(title="Morellatops Egg", description="This recipe is used to make Kibble (Morellatops egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Morellatops Egg \n \t 1x Savoroot \n \t 50x Chitin \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Thorny Dragon", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('MOSCHOPS EGG') or message.content.upper().endswith('29'):
            embed = discord.Embed(title="Moschops Egg", description="This recipe is used to make Kibble (Moschops Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Moschops Egg \n \t 1x Savoroot \n \t 1x Cooked Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Purlovia", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('MOTH EGG') or message.content.upper().endswith('30'):
            embed = discord.Embed(title="Moth Egg", description="This recipe is used to make Kibble (Moth Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Moth Egg \n \t 1x Citronal \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="\u200b", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('OVIRAPTOR EGG') or message.content.upper().endswith('31'):
            embed = discord.Embed(title="Oviraptor Egg", description="This recipe is used to make Kibble (Oviraptor Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Oviraptor Egg \n \t 1x Longrass \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Megalosaurus", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('PACHY EGG') or message.content.upper().endswith('32'):
            embed = discord.Embed(title="Pachy Egg", description="This recipe is used to make Kibble (Pachy egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Pachy Egg \n \t 1x Citronal \n \t 1x Cooked Meat \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Paracer", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('PACHYRHINO EGG') or message.content.upper().endswith('33'):
            embed = discord.Embed(title="Pachyrhino Egg", description="This recipe is used to make Kibble (Pachyrhino Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Pachyrhino Egg \n \t 1x Citronal \n \t 1x Cooked Prime Fish Meat \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Baryonyx", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('PARASAUR EGG') or message.content.upper().endswith('34'):
            embed = discord.Embed(title="Parasaur Egg", description="This recipee is used to make Kibble (Parasaur egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Parasaur Egg \n \t 1x Longrass \n \t 1x Cooked Meat or Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Raptor", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('PEGOMASTAX EGG') or message.content.upper().endswith('35'):
            embed = discord.Embed(title="Pegomastax Egg", description="This recipe is used to make Kibble (Pegomastax Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Pegomastax Egg \n \t 1x Citronal \n \t 1x Raw Prime Fish Meat \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Ichthyornis, Pelagornis", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('PELAGORNIS EGG') or message.content.upper().endswith('36'):
            embed = discord.Embed(title="Pelagornis Egg", description="This recipe is used to make Kibble (Pelagornis Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Pelagornis Egg \n \t 1x Citronal \n \t 10x Chitin \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Archaeopteryx", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('PTERANODON EGG') or message.content.upper().endswith('37'):
            embed = discord.Embed(title="Pteranodon Egg", description="This recipe is used to make Kibble (Pteranodon egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Pteranodon Egg \n \t 1x Rockarrot \n \t 1x Cooked Meat or Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Carbonemys", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('PULMONOSCORPIOUS EGG') or message.content.upper().endswith('38'):
            embed = discord.Embed(title="Pulmonoscorpious Egg", description="This recipe is used to make Kibble (Pulmonoscorpius Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Pulmonoscorpious Egg \n \t 1x Longrass \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Rex, Beelzebufo", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('QUETZAL EGG') or message.content.upper().endswith('39'):
            embed = discord.Embed(title="Quetzal Egg", description="This Recipe is used to make Kibble (Quetzal Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Quetzal Egg \n \t 3x Rockarrot \n \t 3x Prime Meat Jerky \n \t 100x Mejoberries \n \t 120x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Mosasaurus, Giganotosaurus, Dimetrodon", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('RAPTOR EGG') or message.content.upper().endswith('40'):
            embed = discord.Embed(title="Raptor Egg", description="This recipe is used to make Kibble (Raptor egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Raptor Egg \n \t 1x Longrass \n \t 1x Cooked Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Mammoth", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('REX EGG') or message.content.upper().endswith('41'):
            embed = discord.Embed(title="Rex Egg", description="This recipe is used to make Kibble (Rex egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Rex Egg \n \t 1x Longrass \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Plesiosaur, Quetzal", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('ROCK DRAKE EGG') or message.content.upper().endswith('42'):
            embed = discord.Embed(title="Rock Drake Egg", description="This recipe is used to make Kibble (Rock Drake egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Rock Drake Egg \n \t 5x Ascerbic Mushroom \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="\u200b", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('SARCO EGG') or message.content.upper().endswith('43'):
            embed = discord.Embed(title="Sarco Egg", description="This recipe is used to make Kibble (Sarco Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Sarco Egg \n \t 1x Rockarrot \n \t 1x Cooked Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Stego", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('SPINO EGG') or message.content.upper().endswith('44'):
            embed = discord.Embed(title="Spino Egg", description="This recipe is used to make Kibble (Spino egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Spino Egg \n \t 1x Savoroot \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Megalodon", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('STEGO EGG') or message.content.upper().endswith('45'):
            embed = discord.Embed(title="Stego Egg", description="This recipe is used to make Kibble (Stego egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Stego Egg \n \t 1x Citronal \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Argentavis", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('TAPEJARA EGG') or message.content.upper().endswith('46'):
            embed = discord.Embed(title="Tapejara Egg", description="This recipe is used to make Kibble (Tapejara Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Tapejara Egg \n \t 1x Rockarrot \n \t 1x Cooked Prime Meat \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Kaprosuchus", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('TERROR BIRD EGG') or message.content.upper().endswith('47'):
            embed = discord.Embed(title="Terror Bird Egg", description="This recipe is used to make Kibble (Terror Bird egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Terror Bird Egg \n \t 1x Citronal \n \t 1x Cooked Meat or Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="hi2", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('THERIZINO EGG') or message.content.upper().endswith('48'):
            embed = discord.Embed(title="Therizino Egg", description="This recipe is used to make Kibble (Therizino Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Therizino Egg \n \t 1x Citronal \n \t 1x Angler Gel \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Basilosaurus", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('THORNY DRAGON EGG') or message.content.upper().endswith('49'):
            embed = discord.Embed(title="Thorny Dragon Egg", description="This recipe is used to make Kibble (Thorny Dragon egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Thorny Dragon Egg \n \t 1x Savoroot \n \t 1x Cooked Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Lymantria", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('TITANOBOA EGG') or message.content.upper().endswith('50'):
            embed = discord.Embed(title="Titanoboa Egg", description="This recipe is used to make Kibble (Titanoboa Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Titanoboa Egg \n \t 1x Longrass \n \t 1x Cooked Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Gigantopithecus, Dunkleosteus, Thylacoleo", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('TRIKE EGG') or message.content.upper().endswith('51'):
            embed = discord.Embed(title="Trike Egg", description="This recipe is used to make Kibble (Trike egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Trike Egg \n \t 1x Savoroot \n \t 1x Cooked Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Sarco", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('TROODON EGG') or message.content.upper().endswith('52'):
            embed = discord.Embed(title="Troodon Egg", description="This recipe is used to make Kibble (Troodon Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Troodon Egg \n \t 1x Savoroot \n \t 2x Rockarrot \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Equus", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('TURTLE EGG') or message.content.upper().endswith('53'):
            embed = discord.Embed(title="Turtle Egg", description="This recipe is used to make Kibble (Turtle Egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Turtle Egg \n \t 1x Rockarrot \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Bronto, Karkinos", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.upper().endswith('VULTURE EGG') or message.content.upper().endswith('54'):
            embed = discord.Embed(title="Vulture Egg", description="This recipe is used to make Kibble (Vulture egg)", color=0x00ff00)
            embed.add_field(name="Ingredients", value="\u200b \t 1x Vulture Egg \n \t 1x Longrass \n \t 1x Cooked Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", inline=False)
            embed.add_field(name="Dino Taming", value="Morellatops", inline=False)
            await client.send_message(message.channel, embed=embed)
        elif message.content.endswith(''):
            embed = discord.Embed(title="Unsure which kibble recipe you require well let me help choose from:", description="\u200b \n \t 1. Allosaurus Egg \n \t 2. Ankylo Egg \n \t 3. Araneo Egg \n \t 4. Archaeopteryx Egg \n \t 5. Argentavis Egg \n \t 6. Bronto Egg \n \t 7. Baryonyx Egg \n \t 8. Bronto Egg \n \t 9. Carno Egg \n \t 10. Compy Egg \n \t 11. Dilo Egg \n \t 12. Dimetrodon Egg \n \t 13. Dimorph Egg \n \t 14. Diplo Egg \n \t 15. Dodo Egg \n \t 16. Featherlight Egg \n \t 17. Gallimimus Egg \n \t 18. Glowtail Egg \n \t 19. Ichthyornis Egg \n \t 20. Iguanodon Egg \n \t 21. Kairuku Egg \n \t 22. Kaprosuchus Egg \n \t 23. Kentro Egg \n \t 24. Lystrosaurus Egg \n \t 25. Mantis Egg \n \t 26. Megalania Egg \n \t 27. Megalosaurus Egg \n \t 28. Microraptor Egg \n \t 29. Morellatops Egg \n \t 30. Moschops Egg \n \t 31. Moth Egg \n \t 32. Oviraptor Egg \n \t 33. Pachy Egg \n \t 34. Pachyrhino Egg \n \t 35. Parasaur Egg \n \t 36. Pegomastax Egg \n \t 37. Pelagornis Egg \n \t 38. Pteranodon Egg \n \t 39. Pulmonoscorpious Egg \n \t 40. Quetzal Egg \n \t 41. Raptor Egg \n \t 42. Rock Drake Egg \n \t 43. Sarco Egg \n \t 44. Spino Egg \n \t 45. Stego Egg \n \t 46. Tapejara Egg \n \t 47. Terror Bird Egg \n \t 48. Therizino Egg \n \t 49. Thorny Dragon Egg \n \t 50. Titanoboa Egg \n \t 51. Trike Egg \n \t 52. Troodon Egg \n \t 53. Turtle Egg \n \t 54.Vulture Egg", color=0x00BFFF)
            await client.send_message(message.channel, embed=embed)
#                    await client.send_message(message.channel, "Unsure which kibble recipe you require well let me help choose from: \n \t Kibble Ankylo Egg \n \t Kibble Baryonyx Egg \n \t Kibble Carbonemys Egg \n \t Kibble Dilo Egg \n \t Kibble Dimetrodon Egg \n \t Kibble Dimorph Egg \n \t Kibble Dodo Egg \n \t Kibble Featherlight Egg \n \t Kibble Gallimimus Egg \n \t Kibble Glowtail Egg \n \t Kibble Lystrosaurus Egg \n \t Kibble Mantis Egg \n \t Kibble Morellatops Egg \n \t Kibble Pachy Egg \n \t Kibble Parasaur Egg \n \t Kibble Pteranodon Egg \n \t Kibble Raptor Egg \n \t Kibble Rock Drake Egg \n \t Kibble Spino Egg \n \t Kibble Stego Egg \n \t Kibble Terror Bird Egg \n \t Kibble Thorny Dragon Egg \n \t Kibble Trike Egg \n \t Kibble Vulture Egg")


client.run(BotsKey.CB)
