from discord.ext import commands
import discord
from utils import config
import os
import sys, os
sys.path.insert(0, os.path.abspath('..'))

intents = discord.Intents.all()
intents.members = True

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        super().__init__(
            command_prefix=config.prefix, 
            intents=discord.Intents().all(), 
            activity=config.starting_activity,        
            help_command=None
        )
        

        async def setup_hook(self) -> None:
            for filename in os.listdir("./cogs"):
                if filename.endswith('.py'):
                    await self.load_extension(f"cogs.{filename[:-3]}")

        