import discord
import os
import random
from discord.ext import commands

import server

client = commands.Bot(command_prefix='.')

#### LOAD & UNLOAD ####

@client.command()
async def load(context, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(context, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(context, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#Starts the server
server.keep_alive()
#Runs the bot
client.run(os.getenv('TOKEN'))
