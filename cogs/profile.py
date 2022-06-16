import discord
from PIL import Image, ImageColor
from io import BytesIO
import matplotlib.colors as colors
from discord.ext import commands


class profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def profile(self, ctx, member=None):
        if not member:
            member = ctx.author
        roles = discord.utils.find(lambda role: role in member.roles, reversed(ctx.author.roles))
        embed = discord.Embed(title=member.display_name, description="Ваше описание", color=roles.color)
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_author(name="Профиль участника", icon_url=ctx.guild.icon)
        user = await self.bot.fetch_user(member.id)
        if user.banner is None:
            rgb = colors.hex2color(f"{roles.color}")
            color = tuple([int(255 * x) for x in rgb])
            img1 = Image.new('RGB', (600, 80), color)
            byte_io = BytesIO()
            img1.save(byte_io, 'PNG')
            byte_io.seek(0)
            file = discord.File(byte_io, filename="test.png")
            embed.set_image(url="attachment://test.png")
        else:
            file = user.banner
            embed.set_image(url=file)
        embed.set_footer(text="Чтобы изменить профиль введите *!help profile*")
        embed.add_field(name="Ваша репутация", value="0", inline=True)
        embed.add_field(name="Ваши деньги", value="0", inline=True)
        await ctx.send(file=file, embed=embed)


def setup(bot):
    bot.add_cog(profile(bot))
