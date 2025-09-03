# Utiliser une image Python officielle
FROM python:3.12-slim

# Définir le dossier de travail
WORKDIR /app

# Copier les fichiers
COPY requirements.txt .
COPY main.py .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Variables d'environnement optionnelles (token peut être passé depuis Northflank)
ENV DISCORD_TOKEN=""

# Commande de lancement
CMD ["python", "main.py"]
