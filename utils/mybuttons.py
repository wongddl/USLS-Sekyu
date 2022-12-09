
import discord
import asyncio
import random
import asyncio
from utils import embeds,gsheets,config
from discord.utils import get


class Verify(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label = 'Verify', style=discord.ButtonStyle.green, custom_id="1")
    async def Verify(self, interaction: discord.Interaction, Button:discord.ui.Button):
        await interaction.response.send_message(content=f'{random.choice(config.messagess)}', ephemeral=True)
        discord_user = str(interaction.user.id)
        discord_guild = str(config.guild_id)
        member = interaction.user
        registration_data = [[discord_user,discord_guild,'email','code','0']]
        
        await asyncio.sleep(1)
        if interaction.guild_id:
            if discord_user in (item for sublist in gsheets.get_author() for item in sublist):
                datanum = gsheets.get_author().index([f'{str(interaction.user.id)}'])+3
                if not gsheets.get_verify(datanum) == [['1']]:
                    await member.send('You are already on the verification process.', delete_after=5)
                else:
                    await member.send('You have already verified on Rektikano Esports League Server.',delete_after=5)
                    
            else:
                    gsheets.append_user(registration_data)
                    await member.send(embed=embeds.embed_message()[0])
                    await member.send(embed=embeds.embed_message()[1],delete_after=30)

class Guidelines(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label = 'Alliance', style=discord.ButtonStyle.blurple, custom_id="2")
    async def goydloyns(self, interaction: discord.Interaction, Button:discord.ui.Button):
        role = interaction.guild.get_role(config.all_role)
        user = interaction.user
        if role in user.roles:
            msg = discord.Embed(description=f'❌ Removed <@&{config.all_role}> role',color=0xD80000)
            await user.remove_roles(role)
            await interaction.response.send_message(embed=msg,ephemeral=True)
        else:
            msg = discord.Embed(description=f'✅ Added <@&{config.all_role}> role',color=0x24D800)
            await user.add_roles(role)
            await interaction.response.send_message(embed=msg,ephemeral=True)

    @discord.ui.button(label = 'USLS', style=discord.ButtonStyle.green, custom_id="3")
    async def test(self, interaction: discord.Interaction, Button:discord.ui.Button):
        msg = discord.Embed(title='For USLS students only',description='Proceed here ➡ <#1024651422500917320>',color=0x0b3434)
        await interaction.response.send_message(embed=msg,ephemeral=True)    