import asyncio
from config import roles
from discord.ext import commands


class automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = self.bot.get_role(975421175582826496)
        await member.add_role(role)


def setup(bot):
    bot.add_cog(automod(bot))
