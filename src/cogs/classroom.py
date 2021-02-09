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
    
    @staticmethod
    def get_role_and_voice_channel(role_and_voice_channel_name):
        """Check to see if role and voice channel exists"""
        
        role_exist = False
        if get(ctx.guild.roles, name=f"{role_and_voice_channel_name}"): role_exist = True
        else: role_exist = False
        
        channel_exist = False
        if get(ctx.guild.voice.channel, name = f"{role_and_voice_channel_name}"): channel_exist = True
        else: channel_exist = False
        
        if role_exist and channel_exist: return True
        elif role_exist == False and channel_exist == False: return 'role_and_channel_not_exist'
        elif role_exist == False: return 'role_not_exist'
        elif channel_exist == False: return 'channel_not_exist'

    @commands.command(name='classroom', pass_context=True)
    @commands.has_role('Teacher')
    async def classroom(self, room_number, ctx):
        """Add teacher and users to classroom number role."""
        
        # Validate that classroom number voice channel and role exist
        classroom_role_name = f"Classroom{room_number}"
        validate_channel_role_name = get_role_and_voice_channel(classroom_role_name)
        if validate_channel_role_name = 'role_and_channel_not_exist':
            pass
        elif: validate_channel_role_name = 'role_not_exist'
            pass
        elif: validate_channel_role_name = 'channel_not_exist'
            pass
        
        # Validate that there are no users in classroom number voice channel



        # Remove all users from classroom number role

        # Add teacher and selected students to classroom number role


def setup(bot):
    bot.add_cog(Classroom(bot))