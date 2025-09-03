import discord
from discord.ext import commands
import os

# Préfixe
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

# Commande .m <message>
@bot.command()
async def m(ctx, *, message: str):
    try:
        await ctx.message.delete()  # supprime le message de l'utilisateur
    except discord.Forbidden:
        pass  # si le bot n'a pas la permission, on ignore

    await ctx.send(message)  # renvoie le message dans le channel

# Démarrage du bot
bot.run(os.getenv("DISCORD_TOKEN"))
