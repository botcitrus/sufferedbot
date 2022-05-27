import asyncio
from config import roles
from discord.ext import commands


class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role(roles['Admin'], roles['Moderator'])
    async def clear(self, ctx, amount: int):
        if not amount:
            await ctx.send("Вы не указали кол-во сообщений")
        else:
            await ctx.channel.purge(limit=amount)
            msg = await ctx.send("*Сообщения удалены...*")
            await asyncio.sleep(2)
            await msg.delete()


def setup(bot):
    bot.add_cog(moderation(bot))
