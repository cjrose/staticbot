###
### staticbot.py Copyright 2021 Cody Rose
###

import discord
from discord.ext import commands
from bot_token import TOKEN
import random


description = '''A simple bot focused on fun and utility'''
cogs = ['utils']

bot = commands.Bot(command_prefix='.', description=description)

for cog in cogs:
    bot.load_extension('cogs.'+cog)

@bot.event
async def on_ready():
    print('Logged in as: {0.name}#{0.discriminator} -- {0.id}'.format(bot.user))

    guilds = 'Active in the following servers:\n'
    for guild in bot.guilds:
        guilds += '\t{0.name} - {0.id}\n'.format(guild)
    
    print(guilds)

bot.run(TOKEN)