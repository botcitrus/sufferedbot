import asyncio

import discord

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

    @commands.command()
    @commands.has_any_role(roles['Admin'], roles['Moderator'])
    async def ban(self, ctx, member, *, reason):
        if not member:
            embed1 = discord.Embed(title="Неправильное использование команды", color=0xff4d4d)
            embed1.set_author(name="Ошибка",
                             icon_url="https://cdn.discordapp.com/attachments/976450230197305435/976450304478416896"
                                      "/chat.png")
            embed1.add_field(name="Пример:", value="`!ban <@пользователь> <причина>`", inline=False)
            msg = await ctx.send(embed=embed1)
            await asyncio.sleep(2)
            await msg.delete()
        else:
            embed = discord.Embed(color=0xffee33)
            embed.set_author(name=f"{ctx.author.name} забанил пользователя", icon_url=ctx.author.avatar.url)
            embed.add_field(name="Пользователь:", value=member.name, inline=True)
            embed.add_field(name="Причина:", value=reason, inline=True)
            await member.ban(reason=reason)
            await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(moderation(bot))
