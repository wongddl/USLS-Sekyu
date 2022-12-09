from discord.ext import commands
import discord
from utils import mybuttons
from utils.bot import Bot
from utils import gsheets,config
from discord.ui import Button
bot=Bot()

emtitle = " "

prefix = config.prefix
class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.tree.command(name='bulig',description = "Sends USLS Sekyu music command list")
    async def bulig(self,interaction: discord.Integration):
        em = discord.Embed(title=f'/Bulig - USLS Sekyu command lists - prefix "~!"', description=f'''
        ‎
        **=================== 🎵 MUSIC COMMANDS 🎵 ==================**
        ''', colour=0x0b3434)
        em.add_field(name=f"`{prefix}join`", value="Join the vc that the current user is in")
        em.add_field(name=f"`{prefix}leave`", value="Leave the vc that the current user is in")
        em.add_field(name=f"`{prefix}play`", value="Play a song, given either a url or a search term")
        em.add_field(name=f"`{prefix}pause`", value="Pauses current song")
        #em.add_field(name=f"{prefix}Loop", value = "Loops through the current or next song until disabled.")
        em.add_field(name=f"`{prefix}skip`", value="Skips current song")
        em.add_field(name=f"`{prefix}stop`", value="Stops playing and clears queue")
        em.add_field(name=f"`{prefix}clearqueue`", value="Clears the queue")
        em.add_field(name=f"`{prefix}queue`", value="Shows the queue")
        em.add_field(name=f"`.`", value=".")
        em.add_field(name=f"‎", value="**=================== 🎮 GAME COMMANDS 🎮 ==================**", inline=False)
        em.add_field(name=f"`{prefix}battleship @tag`", value="Tag someone to play battleship with")
        em.add_field(name=f"`{prefix}gobblet @tag`", value="Tag someone to play gobblet with")
        em.add_field(name=f"`.`", value=".")
        #em.add_field(name=f"{prefix}Info", value="Shows bot info")
        #em.add_field(name=f"{prefix}Clear", value="Clears the channel by either a certain number of messages, or left blank, the whole channel")

        await interaction.response.send_message(embed = em, ephemeral= True)

    @bot.tree.command(name="anon",description = "Sends an anon message here on Rekt Discord",)
    async def anon(self,interaction: discord.Integration, type_here:str):
        gsheets.get_anonmsgnum()
        anonnum = int(str(gsheets.get_anonmsgnum()).strip('[]').replace('\'', ''))+1
        gsheets.update_anonmsgnum(anonnum)
        channel = interaction.channel
        if (anonnum % 2) == 0:
            colorsz = 0x084545
        else:
            colorsz = 0x147878
        embedded_msg = discord.Embed(title=f'Rektikano Freedom Wall Message #{anonnum}',description=f'{type_here}', color = colorsz)
        embedded_msg.set_footer(text='command: f"/anon" ')
        await interaction.response.send_message(f'Rektikano Freedom Wall Message #{anonnum} was sent',ephemeral=True)
        message = await channel.send(embed=embedded_msg)
        await message.add_reaction('💚')

    # @bot.tree.command(name='verifytest')
    # async def verifytest(self, interaction: discord.Interaction):
    #     await interaction.response.send_message(view=mybuttons.Verify())
    
    # @bot.tree.command(name='guidelinestest')
    # async def guidelinestest(self, interaction: discord.Interaction):
    #     link = Button(label="Need Help❔", url='https://discord.com/channels/758702859717312592/1024625154086682686', style=discord.ButtonStyle.link)
    #     view = mybuttons.Guidelines()
    #     view.add_item(link)
    #     await interaction.response.send_message(view=view)


async def setup(bot):
    bot.add_view(mybuttons.Verify(),message_id=config.verify_button)
    bot.add_view(mybuttons.Guidelines(),message_id=config.guidelines_button)
    await bot.add_cog(Slash(bot))
