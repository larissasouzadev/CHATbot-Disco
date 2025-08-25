import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()  
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot("!",intents=intents)

@bot.event
async def on_ready():
    print("Bot online!")

# saudações
@bot.command()
async def greet(ctx):
    name = ctx.author.name
    await ctx.reply(f" ✦•┈๑⋅⋯ ⋯⋅๑┈•✦ Óla companheiro {name}, Tudo bem?")
# repete texto
@bot.command()
async def speak(ctx:commands.Context, * , text):
    await ctx.send(text)
# bem vindo ao novo user
@bot.command()
async def on_member_join(member:discord.Member):
# pega id do canal 
    channel = bot.get_channel(1404469031397888030)
    await channel.send(f"{member.mention}  ˗ˏˋ ꒰ 🍓🍒🍄 ꒱ ˎˊ˗ se juntou ao nosso partido!")
# reação e marca user
@bot.command()
async def on_reaction_add(reaction:discord.Reaction, member:discord.Member):
    await reaction.message.reply(f"O membro {member.name} reagiu a messagem com {reaction.emoji}")
    
    # ping
@bot.command()
async def ping (ctx):
    latency = round(bot.latency * 1000)
    embed  = discord.Embed(
        title = "⋆｡‧˚ʚ🍓ɞ˚‧｡⋆ Pong!",
        description=f" Latência do bot: **{latency}ms**",
        color=discord.Color.green() if latency <  150 else discord.Color.red()
    )
    await ctx.send(embed=embed)
    
    # ajuda
@bot.command()
async def helping(ctx):
    commands = """
    
    ⛧°。 ⋆༺♱༻⋆。 °⛧ Comandos disponiveis: ⛧°。 ⋆༺♱༻⋆。 °⛧
        '!greet -> comprimenta user.
        '!speak -> repete texto inserido pelo user.
        '!ping -> Mostra a latência do Bot.
        '!help -> Mostra comandos disponiveis.
        '!soma -> Mostra a soma de dois números.
        '!ban -> Banir membro.
        '!kick -> Dar kick em membro folgado.
        '!unban -> Desbanir usuário.
        '!clear -> Limpar o chat. 
        '!view_avatar ->Mostra avatar do membro.
        
        """
    await ctx.send(commands)
    # soma
    
    
@bot.command()
async def soma(ctx, a:int, b:int):
    await ctx.send(f"A soma de {a} + {b} é {a + b} ⟡ ")
    # ban
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, motivo :str = "Não especificado" ):
    try:
        await member.ban(reason=motivo)
        await ctx.send(f"O membro folgado  {member.mention} foi **BANIDO**!/nMotivo:{motivo} ")
    except Exception as e:
        await ctx.send (f" Não foi possivel banir {member.mention}. ERRO:{e}")
    
    # kick
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick (ctx, member:discord.member, *, motivo: str = "Não específicado"):
    try:
        await member.kick(reason=motivo)
        await ctx.send(f"💣💣💣💣O membro  {member.mention} foi expulso do server por {motivo} ")
    except Exception as  e:
        await ctx.send(f"Não foi possível dar kick no membro {member.mention}. ERRO:{e}")  
  
    # unban 
@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, user:str ):
    
    banned_users = await ctx.guild.bans()
    name, discriminator = user.split("#")
    
    for ban_entry in banned_users:
        usuario = ban_entry.user
        
        if (usuario.name, usuario.discriminator) ==(name, discriminator):
            await ctx.guild.unban(usuario)
            await ctx.send(f" 🔓 {usuario} foi desbanido com sucesso ou não! ")
            return 
        await ctx.send(f"❌ Usuário {usuario} não encontrado ma lista de bans!")
    # clear
@bot.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, quantidade: int):
    if quantidade < 1:
        await ctx.send("⚠️ Informe um número válido maior que 0.")
        return

    deletadas = await ctx.channel.purge(limit=quantidade + 1)  # +1 para apagar o comando também
    await ctx.send(f"🧹 Apaguei {len(deletadas) - 1} mensagens!", delete_after=5)
# mostra ft do usuario
@bot.command()
async def view_avatar(ctx, member:discord.Member = None):
    try:
        membro = member or ctx.author
        embed = discord.Embed(
            title=f" ./づ~ 🍓Avatar de {membro} 👀",
            color = discord.Color.red()
            
        )
        embed.set_image(url=membro.display_avatar.url)  # mostra avatar (ou padrão)
        embed.set_footer(text=f"Pedido por {ctx.author}", icon_url=ctx.author.display_avatar.url)

        await ctx.send(embed=embed)
        return
    except Exception as e:
       if member not in discord.Member:
           await ctx.send(f"Não encontrei o membro {membro} nesse server!.ERRO:{e}")
           
           

# memes
# musicas do perfil
# programção 
# members servidores
# xinga user ao sair
# inicia o bot
bot.run(TOKEN)


