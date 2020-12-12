import discord
from discord.ext import commands

popping_paper = """
Here is some popping paper -
||Pop|| ||Pop|| ||Pop|| ||Pop|| ||Pop||
||Pop|| ||Pop|| ||Pop|| ||Pop|| ||Pop||
||Pop|| ||Pop|| ||Pop|| ||Pop|| ||Pop||
||Pop|| ||Pop|| ||Pop|| ||Pop|| ||Pop||
||Pop|| ||Pop|| ||Pop|| ||Pop|| ||Pop||
"""


class SmallGames(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.popping_paper = popping_paper

    # commands
    #### POP ####
    @commands.command()
    async def pop(self, context):
        await context.send(self.popping_paper)


def setup(client):
    client.add_cog(SmallGames(client))
