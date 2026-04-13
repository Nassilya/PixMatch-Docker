# Utilisation d'une image Python légère
FROM python:3.10-slim

# On définit le dossier de travail
WORKDIR /app

# Installation des dépendances (en premier pour gagner du temps au build)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# On copie le dossier app qui contient tes scripts .py
COPY ./app ./app

# On expose le port par défaut de Streamlit
EXPOSE 8501

# Commande pour lancer Streamlit
# On pointe vers app/main_frontend.py car on a copié le dossier
CMD ["streamlit", "run", "app/main_frontend.py", "--server.port=8501", "--server.address=0.0.0.0"]