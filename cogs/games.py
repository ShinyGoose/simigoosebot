import discord
from discord.ext import commands
from lists import answers, popping_paper


class SmallGames(commands.Cog):

    def __init__(self, client):
      self.client = client
      self.popping_paper = popping_paper

    # commands
    #### POP ####
    @commands.command()
    async def pop(self, context):
      await context.send(self.popping_paper)

    #### 8 BALL ####
    @commands.command(aliases=['8ball', 'eightball'])
    async def _8ball(self, context, *, question='no question'):
        # await context.send(f'Q: {question}\nA: {rd.choice(answers)}')

        embed=discord.Embed() #title= Magic 8Ball, color=0xadff2f
        # embed.description = f'Q: {question}\nA: {rd.choice(answers)}'
        embed.title= 'Magic 8Ball'
        embed.color= 0xadff2f

        embed.add_field(name=f"Q: {question}", value=f"A: {rd.choice(answers)}", inline=False)

        # context.message.author.avatar_url
        embed.set_thumbnail(url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.thestar.com.my%2Ftech%2Ftech-news%2F2020%2F02%2F05%2Fpc-download-charts-temtem-tops-steam-desktop-goose-flips-untitled-goose-game-concept&psig=AOvVaw0nO1-0HYp630m-I2H2SSL8&ust=1608203854977000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLCG7Kyw0u0CFQAAAAAdAAAAABAD")

        embed.set_footer(text="the all knowing goose has answered")

        await context.send(embed=embed)

def setup(client):
    client.add_cog(SmallGames(client))
