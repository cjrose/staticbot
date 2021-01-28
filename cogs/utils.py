import discord
from discord.ext import commands

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command()
    async def add(self, ctx, first: float, second: float):
        """Adds two numbers together"""
        await ctx.message.reply('{0} + {1} = {2}'.format(first, second, first + second), mention_author=True)
    
    @commands.command()
    async def divide(self, ctx, first: float, second: float):
        """Divides two numbers"""
        if second == 0:
            await ctx.message.reply('You cannot divide by zero')
            return
        await ctx.message.reply('{0} / {1} = {2}'.format(first, second, first / second), mention_author=True)
    
    @commands.command()
    async def multiply(self, ctx, first: float, second: float):
        """Multiplies two numbers"""
        await ctx.message.reply('{0} x {1} = {2}'.format(first, second, first * second), mention_author=True)
    
    @commands.command()
    async def subtract(self, ctx, first: float, second: float):
        """Subtracts two numbers"""
        await ctx.message.reply('{0} - {1} = {2}'.format(first, second, first - second), mention_author=True)

def setup(bot):
    bot.add_cog(Utils(bot))