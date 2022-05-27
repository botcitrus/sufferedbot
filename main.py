import discord
import os
import io
import contextlib
import textwrap
from config import settings
from traceback import format_exception
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents, debug_guilds=[975324228817657866])

for f in os.listdir('./cogs'):
    if f.endswith('.py'):
        client.load_extension(f'cogs.{f[:-3]}')
        print(f"{f} loaded")


def clean_code(content):
    if content.startswith("```") and content.endswith("```"):
        return "\n".join(content.split("\n")[1:])[:-3]
    else:
        return content


@client.command(name="eval", aliases=["exec"])
async def _eval(ctx, *, code):
    code = clean_code(code)

    local_variables = {
        "discord": discord,
        "commands": commands,
        "bot": client,
        "ctx": ctx,
        "channel": ctx.channel,
        "author": ctx.author,
        "guild": ctx.guild,
        "message": ctx.message
    }

    stdout = io.StringIO()

    with contextlib.redirect_stdout(stdout):
        exec(
            f"async def func():\n{textwrap.indent(code, '    ')}", local_variables,
        )

        obj = await local_variables["func"]()
        result = f"{stdout.getvalue()}"
    await ctx.send(result)


client.run(settings['token'])
