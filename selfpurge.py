import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

client = commands.Bot(command_prefix='!', intents=intents) # this is the prefix u can change it whenever u want(u can change the client too)

@client.command()
async def selfpurge(ctx, count: int):
    await ctx.message.delete() 

    messages = await ctx.channel.history(limit=count).flatten()

    own_messages = [message for message in messages if message.author == ctx.author]

    for message in own_messages:
        await message.delete()

    await ctx.send(f"Deleted {len(own_messages)} of your recent messages.")
