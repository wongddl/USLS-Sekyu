import discord
from discord.ext import commands
from discord.utils import get
from sendgrid import SendGridAPIClient
import random

from utils import embeds,gsheets,config,utilutil




class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        message_content = message.content.strip()
        print(message.author,':',message_content)
        guild = discord.utils.find(lambda g: g.id == config.guild_id, self.bot.guilds)
        role = get(guild.roles, id=config.verified_id)
        author = guild.get_member(message.author.id)
        if message.channel.type == discord.ChannelType.private:
            if str(message.author.id) in (item for sublist in gsheets.get_author() for item in sublist):
                if not message_content in (item for sublist in gsheets.get_email() for item in sublist):
                    datanum = gsheets.get_author().index([f'{str(message.author.id)}'])+3
                    if gsheets.get_verify(datanum) == [['0']]:
                        if message_content[-11:] == config.emaildomain:
                            random_code = random.randint(100000, 999999) #code generated
                            gsheets.update_email(datanum,message_content)
                            gsheets.update_code(datanum,random_code)
                            try:
                                sg = SendGridAPIClient(gsheets.SENDGRID_API_KEY)
                                response = sg.send(utilutil.emailmessage(message_content,random_code))
                                print('VERIFICATION CODE SENT')
                                await message.channel.send(embed=embeds.embed_message()[4],view = embeds.embed_sent_button())
                                await message.channel.send(embed=embeds.embed_message()[2],delete_after=30)
                            except:
                                await message.channel.send(embed=discord.Embed(description='Email failed to send', color = 0xFF0000), delete_after = 5)
                        elif message_content.isnumeric():
                            try:
                                    datanum_code = gsheets.get_code().index([f'{str(message_content)}'])+3
                                    if datanum == datanum_code:
                                        await author.add_roles(role)
                                        gsheets.update_verified(datanum)
                                        await message.channel.send(embed=embeds.embed_message()[3])
                                    else:
                                        await message.channel.send(embed=embeds.embed_invalid()[1],delete_after = 5)

                                
                            except:
                                await message.channel.send(embed=embeds.embed_invalid()[1],delete_after = 5)
                        elif '@' in message_content:
                            await message.channel.send(embed=embeds.embed_invalid()[0],delete_after = 5)
                        else:
                            await message.channel.send(embed=embeds.embed_invalid()[0],delete_after = 5)
                else:
                    await message.channel.send(embed=embeds.embed_invalid()[0],delete_after = 5)
            else:
                await message.channel.send(embed=discord.Embed(description='You have not received a verification process from the server yet.', color = 0xFF0000), delete_after = 5)


async def setup(bot):
    await bot.add_cog(OnMessage(bot))