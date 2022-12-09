from discord.ext import commands, tasks
import discord
import random
from utils import config

class Load(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.statusLooper.start()
        self.memberCount.start()
        self.onlineMemberCount.start()
        print('We have logged in as {0.user}'.format(self.bot))
        try:
            synced = await self.bot.tree.sync()
            print(f'synced {len(synced)} command(s)')
        except Exception as e:
            print(e)
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="gate 2"))

    @tasks.loop(seconds=20)
    async def memberCount(self):
        for guild in self.bot.guilds:
            for vc in guild.voice_channels:
                if vc.id in config.total_members_vc_ids and vc.name != f'🟩 Members: {guild.member_count}':
                    await vc.edit(name = f'🟩 Rekt Members: {guild.member_count}')
                    break

    @tasks.loop(seconds=10)
    async def onlineMemberCount(self):
        for guild in self.bot.guilds:
            for vc in guild.voice_channels:
                if vc.id in config.online_members_vc_ids:
                    members = guild.members
                    onlineMembers = [member for member in members if member.status in [discord.Status.online, discord.Status.idle, discord.Status.do_not_disturb]]
                    if vc.id in config.online_members_vc_ids and vc.name != f'🟢 Online: {len(onlineMembers)}':
                        await vc.edit(name = f'🟢 Online: {len(onlineMembers)}')

    @tasks.loop(seconds=10)
    async def statusLooper(self):

        opt = random.randint(1,4)
        if opt == 1:
            await self.bot.change_presence(activity=discord.Streaming(name=("REKTIKANO"), url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
        elif opt == 2:
            await self.bot.change_presence(activity=discord.Streaming(name=("gate 1"), url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
        elif opt == 3:
            await self.bot.change_presence(activity=discord.Streaming(name=("/bulig"), url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
        elif opt == 4:
            await self.bot.change_presence(activity=discord.Streaming(name=("gate 2"), url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))

async def setup(bot):
    await bot.add_cog(Load(bot))