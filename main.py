import os
import discord
from discord.ext import commands

# 🔐 Récupère le token depuis une variable d'environnement
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix=".", intents=intents)

# ID du rôle requis
ROLE_ID = 1360976279540596736


@bot.event
async def on_ready():
    print(f"{bot.user} est connecté ✅")


@bot.command()
async def m(ctx, *, message: str = None):
    """-"""
    role = ctx.guild.get_role(ROLE_ID)
    if role is None:
        return  # rôle introuvable, on fait rien

    if ctx.author.top_role >= role:
        files = [await attachment.to_file() for attachment in ctx.message.attachments]
        # Si pas de texte mais des fichiers -> on envoie juste les fichiers
        if message:
            await ctx.send(content=message, files=files)
        elif files:
            await ctx.send(files=files)
        await ctx.message.delete()  # supprime le message d'origine
    else:
        return  # pas le rôle → silence total


bot.run(TOKEN)
