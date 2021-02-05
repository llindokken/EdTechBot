import os
import discord
from discord.ext import commands
from discord.utils import get
from datetime import datetime
import json
import requests

class Classroom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='classroom', pass_context=True)
    @commands.has_role('Teacher')
    async def classroom(self, room_number, ctx):
        """Add teacher and users to classroom number role."""
        
        # Validate that classroom number voice channel and role exist
        
        # Validate that there are no users in classroom number voice channel

        # Remove all users from classroom number role

        # Add teacher and selected students to classroom number role
        

def setup(bot):
    bot.add_cog(Classroom(bot))