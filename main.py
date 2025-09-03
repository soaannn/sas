import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN manquant")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

# ID du rôle minimum requis
ROLE_MIN_ID = 1396961119930683427

def has_min_role(member: discord.Member):
    """
    Vérifie si l'utilisateur a le rôle requis ou un rôle plus haut dans la hiérarchie
    """
    min_role = member.guild.get_role(ROLE_MIN_ID)
    if not min_role:
        return False  # rôle introuvable
    for role in member.roles:
        if role.id == ROLE_MIN_ID or role.position > min_role.position:
            return True
    return False

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user} (id={bot.user.id})")

@bot.command()
async def m(ctx, *, message: str):
    # Vérifie le rôle
    if not has_min_role(ctx.author):
        return  # NE FAIT RIEN si l'utilisateur n'a pas le rôle requis

    try:
        await ctx.message.delete()
    except discord.Forbidden:
        pass

    await ctx.send(message)

bot.run(TOKEN)
