import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from logger import logger


# Load environment variables at the start
load_dotenv()
# Access your environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


# Initialize Discord client
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
    

# Run the Discord bot
bot.run(DISCORD_TOKEN)