import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot ist online als {bot.user}')

@bot.command()
async def gamble(ctx):
    await ctx.send("Du hast gewonnen!")

bot.run(os.getenv("TOKEN"))
