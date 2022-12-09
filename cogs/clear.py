from discord.ext import commands
import discord
import asyncio

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='clear',aliases=['c'],help='Clears the current text channel')
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount : int = None):
        global confirmMsgID, confirmMsgUserID
        print('yes')
        if amount is None:

            message = discord.Embed(title="React to this message with :no_entry_sign: to confirm clearing the whole text channel. (This message automatically deletes after 5 seconds)",
                colour=discord.Color.purple()).set_footer(text=f'Requested by {ctx.author.name}')
            confirmMsg = await ctx.channel.send(embed=message)

            await confirmMsg.add_reaction('\N{NO ENTRY SIGN}')
            confirmMsgID = confirmMsg.id
            confirmMsgUserID = ctx.author.id
            return
        
        if isinstance(amount, int) and amount > 0:
            print('right here')
            await ctx.channel.purge(limit=amount+1)

            em = discord.Embed(title=f"**{amount}** messages were deleted", colour=discord.Color.purple())
            em.set_footer(text=f"Requested by {ctx.author.name}")

            delMsg = await ctx.channel.send(embed=em)
            await asyncio.sleep(3)
            await delMsg.delete()
        else:
            em = discord.Embed(title=f"Please specify a valid number of messages to delete", colour=discord.Color.purple())
            em.set_footer(text=f"Requested by {ctx.author.name}")

            return await ctx.send(embed=em)
            
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        try: confirmMsgID
        except NameError: return
        if reaction.message.id == confirmMsgID and reaction.emoji == '\N{NO ENTRY SIGN}' and user.id != self.bot.user.id and user.id == confirmMsgUserID:
            await reaction.message.channel.purge(limit=None)

            em = discord.Embed(title=f"This channel was cleared", colour=discord.Color.blurple())
            em.set_footer(text=f"Requested by {user.name}")

            delMsg = await reaction.message.channel.send(embed=em)
            await asyncio.sleep(3)
            return await delMsg.delete()

async def setup(bot):
    await bot.add_cog(Clear(bot))