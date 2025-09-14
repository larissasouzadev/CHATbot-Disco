import discord
from discord.ext import commands
from discord import app_commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(name="oi", description="Responde com uma saudação")
    async def oi(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Olá, {interaction.user.mention}! 👋")
# bem vindo ao novo user
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(1404469031397888030)
        embed = discord.Embed(
            title = f"{member.name} se juntouu ao Partido!!"
            image = ""
            color=discord.Color.red()
        )
        embed.set_image(url=member.display_avatar.url) 
        embed.set_image(url="attachment://gato2.jpg")
        file = discord.File("imgs/gato2.jpeg", filename="gato2.jpg")
        if channel:
            await channel.send(embed=embed)
# event quando user sai do server
    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel_logs = discord.utils.get(member.guild.text_channels, name="logs")
        if channel_logs:
            embed = discord.Embed(
                title=f"{member.name} saiu do nosso partido!",
                color=discord.Color.red()
            )
            embed.set_image(url=member.display_avatar.url)
            embed.set_image(url="attachment://gato3.jpg")
            file = discord.File("imgs/gato3.jpg", filename="gato3.jpg")
            embed.add_field(name="Motivo", value="Não é confiável!!!!!", inline=False)
            await channel_logs.send(embed=embed)
# quando um user reage 
    @commands.Cog.listener()
    async def on_reaction_add(self,reaction:discord.Reaction, member:discord.Member):
        await reaction.message.reply(f"O membro {member.name} reagiu a messagem com {reaction.emoji}")
async def setup(bot: commands.Bot):
    await bot.add_cog(Events(bot))
