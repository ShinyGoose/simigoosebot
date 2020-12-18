import discord
import random as rd
import math

from lists import stuff, math_formulas
from discord.ext import commands


class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    # events
    @commands.Cog.listener()
    async def on_ready(self):
      await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for commands"))
      print('Ready!')

    # commands
    #### PING ####
    @commands.command()
    async def ping(self, context):
      
        await context.send(f"""🏓Pong!\n\n```apache\n Ping is: {round(self.client.latency * 1000)}ms```""")
    
    #### PONG ####
    @commands.command()
    async def pong(self, context):
        await context.send("🏓Ping!")

    #### READY! ####
    @commands.command()
    async def bot(self, context):
        await context.send("Goose Bot is Ready!")


    #### HONK ####
    @commands.command()
    async def honk(self, context):
        await context.send('Honk!')

    #### RANDOM NUMBER ####
    @commands.command()
    async def random(self, context, lower_limit=0, upper_limit=10):
        await context.send(str(rd.randint(int(lower_limit), int(upper_limit))))

    #### CLEAR ####
    @commands.command()
    async def clear(self, context, amount=5):
      await context.channel.purge(limit=amount+1)

    #### Chemistry ####
    @commands.command()
    async def chemistry(self, context):

        await context.send(f'{rd.choice(stuff)}')

    

    @commands.command(aliases=['maths', 'math', 'formulas', 'meth'])
    async def _maths(self, context):
        embed=discord.Embed()
        embed.title= 'Mathematik'
        embed.color= 0xadff2f

        embed.add_field(name="Formule", value=math_formulas)
        embed.set_footer(text="Gute Sache!")

        await context.send(embed=embed)


    @commands.command(aliases=['delta', 'd'])
    async def _delta(self, context, a, b, c):
        # function that calculates x1, x2
        def solve(a, b, c):
          d = math.sqrt(abs(b**2 - 4*a*c)) # delta = b² - 4ac
          x1 = (-b + d) / (2 * a)
          x2 = (-b - d) / (2 * a)
          return x1, x2, d

        x1, x2, d= solve(int(a), int(b), int(c))

        # displaying the result
        embed=discord.Embed(title='∆ Quick Delta Calculator ∆', color=0x738adb)
        embed.add_field(name='Input', value=f'a={a} b={b} c={c}', inline=True)
        embed.add_field(name='Output', value=f'√∆ = {d} x1= {x1} x2= {x2}', inline=False)
        embed.add_field(name='Result', value=f'{a} * (x- {x1}) * (x- {x2})', inline=False)
        embed.set_footer(text="you're welcome")
        await context.send(embed=embed)

    @commands.command(aliases=['dformulas'])
    async def _delta_formulas(self, context):
        # displaying the result
        embed=discord.Embed(title='∆ Delta Formulas ∆', color=0x738adb)
        embed.add_field(name='Formulas', value='∆ = b² - 4ac \nx1 = (-b - √∆) / (2 * a)\nx2 = (-b + √∆) / (2 * a)\n p = a * (x - x1) * (x - x2)', inline=False)
        embed.set_footer(text="you're welcome")
        await context.send(embed=embed)

    

        


def setup(client):
    client.add_cog(Commands(client))
