import discord
import random as rd
from discord.ext import commands


class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    # events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')

    # commands
    #### PING ####
    @commands.command()
    async def ping(self, context):
        await context.send(f"{round(self.client.latency * 1000)}ms")

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

    #### Chemestry ####
    @commands.command()
    async def chemestry(self, context):
        stuff = [
            "2Na + F2 -> 2NaF",
            "4SO2 + 2O2 -> 4SO3",
            "Li2O +  H2O -> 2Li OH",
            "2HCl + Mg(OH)2 -> MgCl2 + 2H2O",
            "Ca + 2HNO3 -> Ca(NO3 ) 2 + H2",
            "H2 + I2 -> 2HI",
            "4Al +3O2 -> 2Al2O3",
            "2N H 3 + H2 SO4 -> (NH4 ) SO4",
            "2Na + 2H2O -> 2NaOH + H2",
            "2H3PO4 + 6Na -> 2Na3PO4 + 3H2",
            "Kalium reagiert mit Wasser zu Kaliumhydroxid und Wasserstoff",
            "Magnesiumiodid reagiert mit Schwefelsäure  zu Magnesiumsulfat und Wasserstoffiodid",
            "Calcium reagiert mit Sauerstoff zu Calciumoxid",
            "Aluminium reagiert mit Brom zu Aluminiumbromid.",
            "Chlorwasserstoff reagiert mit Calciumcarbonat zu Calciumchlorid, Kohlenstoffdioxid und Wasser",
            "Sn2 and Sn1 reactions are not a clear-cut case one of the other. It's a spectrum. -Polarity is a continuum. There are very few molecules that you can say, this is polar and this is non-polar. Polarity is only meaningful in relation to something else. There are also about 4/5 measures of polarity that are determined by highly technical p-chem-y stuff. It's also different depending on whether you are looking at solubility or chromatography or what.",
            "H-bonding. Don't even get me started. When I started my graduate studies my professor gave me an entire BOOK on hydrogen bonding. Two of my professors had a decades long friendly feud about whether or not certain interactions can be called a hydrogen bond. The IUPAC had a committee that met for YEARS to figure out what can and cannot be called hydrogen bonding. This actually goes for all intermolecular interactions.",
            "Deoxyribonucleic acid:\nC15H31N3O13P2",
            "H2O + Na2O2 + Ca(ClO)2 → O2 + NaCl + Ca(OH)2",
            "H2O + Ca3N2 → NH3 + Ca(OH)2",
            "Sn2 and Sn1 reactions are not a clear-cut case one of the other. It's a spectrum. -Polarity is a continuum. There are very few molecules that you can say, this is polar and this is non-polar. Polarity is only meaningful in relation to something else. There are also about 4/5 measures of polarity that are determined by highly technical p-chem-y stuff. It's also different depending on whether you are looking at solubility or chromatography or what.",
            "Sn2 and Sn1 reactions are not a clear-cut case one of the other. It's a spectrum. -Polarity is a continuum. There are very few molecules that you can say, this is polar and this is non-polar. Polarity is only meaningful in relation to something else. There are also about 4/5 measures of polarity that are determined by highly technical p-chem-y stuff. It's also different depending on whether you are looking at solubility or chromatography or what."
        ]

        await context.send(f'{rd.choice(stuff)}')

    #### HONK ####
    @commands.command(aliases=['8ball', 'eightball'])
    async def _8ball(self, context, *, question='no question'):
        answers = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]

        await context.send(f'Q: {question}\nA: {rd.choice(answers)}')


def setup(client):
    client.add_cog(Commands(client))
