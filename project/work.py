import discord
intents=discord.Intents.default()
intents.members=True
from discord.ext import commands

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(">>Bot_Online<<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(774628590896545814)
    await channel.send(f'{member}從山坡上滾下來了')

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(774628590896545814)
    await channel.send(f'再會{member}')

bot.run('token')