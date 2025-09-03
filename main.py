import os
import discord
from discord.ext import commands

TOKEN = os.getenv("MTQxMjgzNDQ1NjQ1NjI2NTczOQ.GN018y.Yzswe0KRahGURBYK-gqjxAbeUhARo0VEZTeBvQ")
if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN manquant")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

ROLE_MIN_ID = 1396961119930683427

def has_min_role(member: discord.Member):
    min_role = member.guild.get_role(ROLE_MIN_ID)
    if not min_role:
        return False
    for role in member.roles:
        if role.id == ROLE_MIN_ID or role.position > min_role.position:
            return True
    return False

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user} (id={bot.user.id})")

@bot.command()
async def m(ctx, *, message: str):
    if not has_min_role(ctx.author):
        return  # NE FAIT RIEN si pas le rôle
    try:
        await ctx.message.delete()
    except discord.Forbidden:
        pass
    await ctx.send(message)

bot.run(TOKEN)
