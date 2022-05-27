import asyncio
from config import roles
import discord
from discord.ext import commands


class automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, name="участник")
        await member.add_roles(role)


def setup(bot):
    bot.add_cog(automod(bot))
