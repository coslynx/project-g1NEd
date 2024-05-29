# logging.py (Python)

import discord
from discord.ext import commands
import json

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logging module is ready.')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Invalid command. Please try again.')

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        # Log deleted messages
        with open('data/moderation_data.json', 'r') as file:
            data = json.load(file)

        if 'deleted_messages' in data:
            data['deleted_messages'].append(message.content)
        else:
            data['deleted_messages'] = [message.content]

        with open('data/moderation_data.json', 'w') as file:
            json.dump(data, file, indent=4)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        # Log edited messages
        with open('data/moderation_data.json', 'r') as file:
            data = json.load(file)

        if 'edited_messages' in data:
            data['edited_messages'].append({'before': before.content, 'after': after.content})
        else:
            data['edited_messages'] = [{'before': before.content, 'after': after.content}]

        with open('data/moderation_data.json', 'w') as file:
            json.dump(data, file, indent=4)

def setup(bot):
    bot.add_cog(Logging(bot))