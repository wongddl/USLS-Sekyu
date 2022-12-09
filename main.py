from utils.bot import Bot
from utils.gsheets import DISCORD_TOKEN
import asyncio
import os


bot = Bot()

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith('.py'):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(DISCORD_TOKEN)

if __name__=="__main__":
    asyncio.run(main())

