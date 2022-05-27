import discord
import datetime
from discord.ext import commands


class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.id == 975327611267981314:
            return
        else:
            guild = message.guild
            channel = guild.get_channel(979047685912928317)
            embed = discord.Embed(color=0x2f3136, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Удаленное сообщение:", value=message.content)
            embed.add_field(name="Чат", value=message.channel.mention, inline=False)
            embed.set_author(name=f"{message.author.name} удалил сообщение", icon_url=message.author.avatar.url)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.id == 975327611267981314:
            return
        else:
            guild = before.guild
            channel = guild.get_channel(979047685912928317)
            embed = discord.Embed(color=0x2f3136, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="До:", value=before.content, inline=True)
            embed.add_field(name="После:", value=after.content, inline=True)
            embed.add_field(name="Чат", value=before.channel.mention, inline=False)
            embed.set_author(name=f"{before.author.name} изменил сообщение", icon_url=before.author.avatar.url)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(979047685912928317)
        embed = discord.Embed(color=0x2f3136, timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f"{member.name} зашел на сервер", icon_url=member.avatar.url)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(979047685912928317)
        embed = discord.Embed(color=0x2f3136, timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f"{member.name} вышел с сервера", icon_url=member.avatar.url)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(979047685912928317)
        embed = discord.Embed(description="Бот запущен", color=0x85c98a, timestamp=datetime.datetime.utcnow())
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Logs(bot))
