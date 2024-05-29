# interface.py (Python)

import discord
from discord.ext import commands

class Interface(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} has connected to Discord!')

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command(name='kick')
    async def kick_user(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} has been kicked.')

    @commands.command(name='ban')
    async def ban_user(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned.')

    @commands.command(name='mute')
    async def mute_user(self, ctx, member: discord.Member):
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.add_roles(muted_role)
        await ctx.send(f'{member.mention} has been muted.')

    @commands.command(name='unmute')
    async def unmute_user(self, ctx, member: discord.Member):
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.remove_roles(muted_role)
        await ctx.send(f'{member.mention} has been unmuted.')

    @commands.command(name='warn')
    async def warn_user(self, ctx, member: discord.Member, *, reason=None):
        # Logic to issue a warning to the user
        await ctx.send(f'{member.mention} has been warned. Reason: {reason}')

def setup(bot):
    bot.add_cog(Interface(bot))