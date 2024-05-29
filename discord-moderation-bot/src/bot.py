# bot.py (Python)

import discord
from discord.ext import commands
import json

# Import other files
import commands
import moderation
import role_management
import logging
import anti_raid
import interface
import alerts

# Load configuration from JSON file
with open('config.json', 'r') as f:
    config = json.load(f)

# Initialize bot
bot = commands.Bot(command_prefix=config['prefix'])

# Bot events
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Add commands
bot.add_cog(commands.Commands(bot))

# Add moderation features
bot.add_cog(moderation.Moderation(bot))

# Add role management features
bot.add_cog(role_management.RoleManagement(bot))

# Add logging features
bot.add_cog(logging.Logging(bot))

# Add anti-raid protection
bot.add_cog(anti_raid.AntiRaid(bot))

# Add user interface
bot.add_cog(interface.Interface(bot))

# Add alerts system
bot.add_cog(alerts.Alerts(bot))

# Run the bot
bot.run(config['token'])