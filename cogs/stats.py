from config import roles
from discord.ext import commands


class stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role(roles['Admin'])
    async def stats(self, ctx):
        member = ctx.guild.member_count
        category = ctx.guild.get_channel(986980872160935956)
        await ctx.guild.create_voice_channel(name=f"👤 Участников: {member}", category=category)

    @commands.Cog.listener()
    async def on_member_join(self, ctx):
        member = ctx.guild.member_count
        channel = ctx.guild.get_channel(986994391082225735)
        await channel.edit(name=f"👤 Участников: {member}")

    @commands.Cog.listener()
    async def on_member_remove(self, ctx):
        channel = ctx.guild.get_channel(986994391082225735)
        await channel.edit(name=f"👤 Участников: {guild.member_count}")

    @commands.Cog.listener()
    async def on_ready(self):
        guild = self.bot.get_guild(975324228817657866)
        channel = guild.get_channel(986994391082225735)
        await channel.edit(name=f"👤 Участников: {guild.member_count}")


def setup(bot):
    bot.add_cog(stats(bot))
