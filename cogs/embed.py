import discord
import json
from PIL import Image
from io import BytesIO
import matplotlib.colors as colors
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

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def test(self, ctx, color):
        int_colour = int(color[1:], 16)
        color1 = color
        embed = discord.Embed(title="**Название сообщения**", description="> Описание сообщения, "
                                                                          "тут может быть любой текст подходящий "
                                                                          "к теме сообщения!", color=int_colour)
        # embed.set_author(name="Название команды")
        # embed.set_thumbnail(url="attachment://sep.png")
        img = Image.open("pics/sep1.png")
        datas = img.getdata()
        new_image_data = []
        rgb = colors.hex2color(f"{color1}")
        color = tuple([int(255 * x) for x in rgb])
        for item in datas:
            if item[1] in list(range(247, 256)):
                new_image_data.append(color)
            else:
                new_image_data.append(item)
        img.putdata(new_image_data)
        byte_io = BytesIO()
        img.save(byte_io, 'PNG')
        byte_io.seek(0)
        file = discord.File(byte_io, filename="test.png")
        embed.set_image(url="attachment://test.png")
        embed.add_field(name="Название", value="Любой текст подходящий к теме сообщения", inline=False)
        embed.add_field(name="Название", value="Любой текст подходящий к теме сообщения", inline=False)
        embed.add_field(name="Название", value="Любой текст подходящий к теме сообщения", inline=False)
        embed.add_field(name="Название", value="Любой текст подходящий к теме сообщения", inline=False)
        embed.add_field(name="Название", value="Любой текст подходящий к теме сообщения", inline=False)
        await ctx.send(file=file, embed=embed)


def setup(bot):
    bot.add_cog(idk(bot))
