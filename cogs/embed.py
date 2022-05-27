import discord
import json
from discord.ext import commands


class idk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def embed(self, ctx, *, arg1):
        response = arg1
        embed = discord.Embed.from_dict(json.loads(response))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(idk(bot))
