import discord
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Autoreact ready')

@client.event
async def on_message(message):
    if message.channel.id == 671080896480149575:
        await message.add_reaction("👍🏼")
        await message.add_reaction("👎🏼")

client.run("NjgzNTA5NjA1NDY4MzQwMjI0.Xl1UGg.QU_NNXMhPgywkq5myUHQQU95qB8")
