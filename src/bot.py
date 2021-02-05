# bot.py
import dotenv
import os
import discord
from discord.ext import commands



dotenv.load('../.env')
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot Command
bot = commands.Bot(command_prefix='!')

bot.load_extension("cogs.classroom")
    
bot.run(TOKEN)