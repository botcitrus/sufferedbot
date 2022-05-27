import asyncio
from config import roles
from discord.ext import commands


class automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message:
            return
# soon


def setup(bot):
    bot.add_cog(automod(bot))
