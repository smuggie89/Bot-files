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
        print ('e_w_k_f')
        if ' ' in message.content.upper():
            if message.content.upper().endswith(kibblename) or (Functions.SplitFunction(message.content, ' ')[1] == kibblenumber):
                print(kibblename + kibblenumber)
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
         for server in client.servers:
             for channel in server.channels:
                 if channel.name == 'recipes':
                    embed = discord.Embed(title="Commands for #recipe channel", description="Ah, so i see you need some help! Let me provide you with some queastions you can ask", color=0x27408B)
                    embed.add_field(name="\u200b \t !kibble", value="\u200b \t gives you a list of all available kibble recipes", inline=False)
                    embed.add_field(name="\u200b \t !kibble <kibble name>", value="\u200b \t provides recipe and details of sepcified kibble", inline=False)
                    embed.add_field(name="\u200b \t !food", value="\u200b \t gives a list of all available food recipes", inline=False)
                    embed.add_field(name="\u200b \t !food <food name>", value="\u200b \t provides details of specified food", inline=False)
                    await client.send_message(channel, embed=embed)

#Kibble Recipes
    if message.content.upper().startswith('!KIBBLE'):
        print ('True')
        if e_w_k_f('ALLOSAURUS EGG', '1'):
            print ('return true')
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
        elif e_w_k_f('DILO EGG', '10'):
            await client.send_message(message.channel, embed=em_k_f("Dilo", "\u200b \t 1x Dilo Egg \n \t 1x Citronal \n \t 1x Cooked Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Ankylo, Doedicurus, Pachy"))
        elif e_w_k_f('DIMETRODON EGG', "11"):
            await client.send_message(message.channel, embed=em_k_f("Dimetrodon", "\u200b \t 1x Dimetrodon Egg \n \t 1x Citronal \n \t 1x Cooked Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Gallimimus"))
        elif e_w_k_f('DIMORPH EGG', "12"):
            await client.send_message(message.channel, embed=em_k_f("Dimorph", "\u200b \t 1x Dimorph Egg \n \t 1x Longrass \n \t 1x Cooked Meat or Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Megaloceros"))
        elif e_w_k_f('DIPLO EGG', '13'):
            await client.send_message(message.channel, embed=em_k_f("Diplo", "\u200b \t 1x Diplo Egg \n \t 1x Savoroot \n \t 1x Rare Flower \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Allosaurus"))
        elif e_w_k_f('DODO EGG', '14'):
            await client.send_message(message.channel, embed=em_k_f("Dodo", "\u200b \t 1x Dodo Egg \n \t 1x Rockarrot \n \t 1x Cooked Meat or Cooked Fish Meat \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Pteranodon, Ichthy, Mesopithecus"))
        elif e_w_k_f('FEATHERLIGHT EGG', '15'):
            await client.send_message(message.channel, embed=em_k_f("Featherlight", "\u200b \t 1x Featherlight Egg \n \t 3x Auric Mushroom \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "\u200b"))
        elif e_w_k_f('GALLIMIMUS EGG', '16'):
            await client.send_message(message.channel, embed=em_k_f("Gallimimus", "\u200b \t 1x Gallimimus Egg \n \t 1x Savoroot \n \t 1x Cooked Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Terror Bird, Castoroides"))
        elif e_w_k_f('GLOWTAIL EGG', '17'):
            await client.send_message(message.channel, embed=em_k_f("Glowtail", "\u200b \t 1x Glowtail Egg \n \t 3x Aquatic Mushroom \n \t 1x Cooked Fish Meat \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "\u200b"))
        elif e_w_k_f('ICHTHYORNIS EGG', '18'):
            await client.send_message(message.channel, embed=em_k_f("Ichthyornis", "\u200b \t 1x Ichthyornis Egg \n \t 1x Savoroot \n \t 1x Rare Flower \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Giant Bee"))
        elif e_w_k_f('IGUANODON EGG', '19'):
            await client.send_message(message.channel, embed=em_k_f("Iguanodon", "\u200b \t 1x Iguanodon Egg \n \t 1x Rare Mushroom \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin","Daeodon"))
        elif e_w_k_f('KAIRUKU EGG', '20'):
            await client.send_message(message.channel, embed=em_k_f("Kairuku", "\u200b \t 1x Kairuku Egg \n \t 1x Savoroot \n \t 1x Cooked Meat or Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Angler"))
        elif e_w_k_f('KAPROSUCHUS EGG', '21'):
            await client.send_message(message.channel, embed=em_k_f("Kaprosuchus", "\u200b \t 1x Kaprosuchus Egg \n \t 1x Savoroot \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "\u200b"))
        elif e_w_k_f('KENTRO EGG', '22'):
            await client.send_message(message.channel, embed=em_k_f("Kentro", "\u200b \t 1x Kentro Egg \n \t 1x Amonite Bile \n \t 1x Golden Hesperornis Egg \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Yutyrannus"))
        elif e_w_k_f('LYSTROSAURUS EGG', '23'):
            await client.send_message(message.channel, embed=em_k_f("Lystrosaurus", "\u200b \t 1x Lystrosaurus Egg \n \t 1x Rockarrot \n \t 1x Cooked Prime Meat or Prime Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Diplodocus"))
        elif e_w_k_f('MANTIS EGG', '24'):
            await client.send_message(message.channel, embed=em_k_f("Mantis", "\u200b \t 1x Mantis Egg \n \t 1x Citronal \n \t 1x Obsidian \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Rock Elemental"))
        elif e_w_k_f('MEGALANIA EGG', '25'):
            await client.send_message(message.channel, embed=em_k_f("Megalania", "\u200b \t 1x Megalania Egg \n \t 1x Giant Bee Honey \n \t 10x Chitin \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Megatherium"))
        elif e_w_k_f('MEGALOSAURUS EGG', '26'):
            await client.send_message(message.channel, embed=em_k_f("Megalosaurus", "\u200b \t 1x Megalosaurus Egg \n \t 1x Rockarrot \n \t 2x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Therizinosaurus"))
        elif e_w_k_f('MICRORAPTOR EGG', '27'):
            await client.send_message(message.channel, embed=em_k_f("Microraptor", "\u200b \t 1x Microraptor Egg \n \t 1x Longrass \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Iguanodon"))
        elif e_w_k_f('MORELLATOPS EGG', '28'):
            await client.send_message(message.channel, embed=em_k_f("Morellatops", "\u200b \t 1x Morellatops Egg \n \t 1x Savoroot \n \t 50x Chitin \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Thorny Dragon"))
        elif e_w_k_f('MOSCHOPS EGG', '29'):
            await client.send_message(message.channel, embed=em_k_f("Moschops", "\u200b \t 1x Moschops Egg \n \t 1x Savoroot \n \t 1x Cooked Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Purlovia"))
        elif e_w_k_f('MOTH EGG', '30'):
            await client.send_message(message.channel, embed=em_k_f("Moth", "\u200b \t 1x Moth Egg \n \t 1x Citronal \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "\u200b"))
        elif e_w_k_f('OVIRAPTOR EGG', '31'):
            await client.send_message(message.channel, embed=em_k_f("Oviraptor", "\u200b \t 1x Oviraptor Egg \n \t 1x Longrass \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Megalosaurus"))
        elif e_w_k_f('PACHY EGG', '32'):
            await client.send_message(message.channel, embed=em_k_f("Pachy", "\u200b \t 1x Pachy Egg \n \t 1x Citronal \n \t 1x Cooked Meat \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Paracer"))
        elif e_w_k_f('PACHYRHINO EGG', '33'):
            await client.send_message(message.channel, embed=em_k_f("Pachyrhino", "\u200b \t 1x Pachyrhino Egg \n \t 1x Citronal \n \t 1x Cooked Prime Fish Meat \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Baryonyx"))
        elif e_w_k_f('PARASAUR EGG', '34'):
            await client.send_message(message.channel, embed=em_k_f("Parasaur", "\u200b \t 1x Parasaur Egg \n \t 1x Longrass \n \t 1x Cooked Meat or Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Raptor"))
        elif e_w_k_f('PEGOMASTAX EGG', '35'):
            await client.send_message(message.channel, embed=em_k_f("Pegomastax", "\u200b \t 1x Pegomastax Egg \n \t 1x Citronal \n \t 1x Raw Prime Fish Meat \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Ichthyornis, Pelagornis"))
        elif ('PELAGORNIS EGG', '36'):
            await client.send_message(message.channel, embed=em_k_f("Pelagornis", "\u200b \t 1x Pelagornis Egg \n \t 1x Citronal \n \t 10x Chitin \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Archaeopteryx"))
        elif e_w_k_f('PTERANODON EGG', '37'):
            await client.send_message(message.channel, embed=em_k_f("Pteranodon", "\u200b \t 1x Pteranodon Egg \n \t 1x Rockarrot \n \t 1x Cooked Meat or Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Carbonemys"))
        elif e_w_k_f('PULMONOSCORPIOUS EGG', '38'):
            await client.send_message(message.channel, embed=em_k_f("Pulmonoscorpious", "\u200b \t 1x Pulmonoscorpious Egg \n \t 1x Longrass \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Rex, Beelzebufo"))
        elif e_w_k_f('QUETZAL EGG', '39'):
            await client.send_message(message.channel, embed=em("Quetzal", "\u200b \t 1x Quetzal Egg \n \t 3x Rockarrot \n \t 3x Prime Meat Jerky \n \t 100x Mejoberries \n \t 120x Fiber \n \t 1x Waterskin", "Mosasaurus, Giganotosaurus, Dimetrodon"))
        elif e_w_k_f('RAPTOR EGG', '40'):
            await client.send_message(message.channel, embed=em_k_f("Raptor", "\u200b \t 1x Raptor Egg \n \t 1x Longrass \n \t 1x Cooked Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Mammoth"))
        elif e_w_k_f('REX EGG', '41'):
            await client.send_message(message.channel, embed=em_k_f("Rex", "\u200b \t 1x Rex Egg \n \t 1x Longrass \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Plesiosaur, Quetzal"))
        elif e_w_k_f('ROCK DRAKE EGG', '42'):
            await client.send_message(message.channel, embed=em_k_f("Rock Drake", "\u200b \t 1x Rock Drake Egg \n \t 5x Ascerbic Mushroom \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "\u200b"))
        elif e_w_k_f('SARCO EGG', '43'):
            await client.send_message(message.channel, embed=em_k_f("Sarco", "\u200b \t 1x Sarco Egg \n \t 1x Rockarrot \n \t 1x Cooked Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Stego"))
        elif e_w_k_f('SPINO EGG', '44'):
            await client.send_message(message.channel, embed=em_k_f("Spino", "\u200b \t 1x Spino Egg \n \t 1x Savoroot \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Megalodon"))
        elif e_w_k_f('STEGO EGG', '45'):
            await client.send_message(message.channel, embed=em_k_f("Stego", "\u200b \t 1x Stego Egg \n \t 1x Citronal \n \t 1x Prime Meat Jerky \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Argentavis"))
        elif e_w_k_f('TAPEJARA EGG', '46'):
            await client.send_message(message.channel, embed=em_k_f("Tapejara", "\u200b \t 1x Tapejara Egg \n \t 1x Rockarrot \n \t 1x Cooked Prime Meat \n \t 2x Mejoberries \n \t 3x Fiber \n \t 1x Waterskin", "Kaprosuchus"))
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
        elif message.content.upper() == ('!KIBBLE'):
            print (message.content.upper())
            embed = discord.Embed(title="Unsure which kibble recipe you require well let me help choose from:", description="\u200b \n \t 1. Allosaurus Egg \n \t 2. Ankylo Egg \n \t 3. Araneo Egg \n \t 4. Archaeopteryx Egg \n \t 5. Argentavis Egg \n \t 6. Bronto Egg \n \t 7. Baryonyx Egg \n \t 8. Bronto Egg \n \t 9. Carno Egg \n \t 10. Compy Egg \n \t 11. Dilo Egg \n \t 12. Dimetrodon Egg \n \t 13. Dimorph Egg \n \t 14. Diplo Egg \n \t 15. Dodo Egg \n \t 16. Featherlight Egg \n \t 17. Gallimimus Egg \n \t 18. Glowtail Egg \n \t 19. Ichthyornis Egg \n \t 20. Iguanodon Egg \n \t 21. Kairuku Egg \n \t 22. Kaprosuchus Egg \n \t 23. Kentro Egg \n \t 24. Lystrosaurus Egg \n \t 25. Mantis Egg \n \t 26. Megalania Egg \n \t 27. Megalosaurus Egg \n \t 28. Microraptor Egg \n \t 29. Morellatops Egg \n \t 30. Moschops Egg \n \t 31. Moth Egg \n \t 32. Oviraptor Egg \n \t 33. Pachy Egg \n \t 34. Pachyrhino Egg \n \t 35. Parasaur Egg \n \t 36. Pegomastax Egg \n \t 37. Pelagornis Egg \n \t 38. Pteranodon Egg \n \t 39. Pulmonoscorpious Egg \n \t 40. Quetzal Egg \n \t 41. Raptor Egg \n \t 42. Rock Drake Egg \n \t 43. Sarco Egg \n \t 44. Spino Egg \n \t 45. Stego Egg \n \t 46. Tapejara Egg \n \t 47. Terror Bird Egg \n \t 48. Therizino Egg \n \t 49. Thorny Dragon Egg \n \t 50. Titanoboa Egg \n \t 51. Trike Egg \n \t 52. Troodon Egg \n \t 53. Turtle Egg \n \t 54.Vulture Egg", color=0x00BFFF)
            await client.send_message(message.channel, embed=embed)
        else:
            print ('Sams Different code return')
            await client.send_message(message.channel, 'Sams Different code return')
#                    await client.send_message(message.channel, "Unsure which kibble recipe you require well let me help choose from: \n \t Kibble Ankylo Egg \n \t Kibble Baryonyx Egg \n \t Kibble Carbonemys Egg \n \t Kibble Dilo Egg \n \t Kibble Dimetrodon Egg \n \t Kibble Dimorph Egg \n \t Kibble Dodo Egg \n \t Kibble Featherlight Egg \n \t Kibble Gallimimus Egg \n \t Kibble Glowtail Egg \n \t Kibble Lystrosaurus Egg \n \t Kibble Mantis Egg \n \t Kibble Morellatops Egg \n \t Kibble Pachy Egg \n \t Kibble Parasaur Egg \n \t Kibble Pteranodon Egg \n \t Kibble Raptor Egg \n \t Kibble Rock Drake Egg \n \t Kibble Spino Egg \n \t Kibble Stego Egg \n \t Kibble Terror Bird Egg \n \t Kibble Thorny Dragon Egg \n \t Kibble Trike Egg \n \t Kibble Vulture Egg")

client.run(BotsKey.CB)
