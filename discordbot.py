from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']

client.event
async def on_message(message):
    if message.content.statswith('kingariempire'):
        role = discord.utils.get(message.guild.roles, name= '国民')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} ようこそ！'
        await message.channel.send(reply)



@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
