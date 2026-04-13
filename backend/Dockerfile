FROM python:3.10-slim

WORKDIR /app

# Dépendances système pour OpenCV, FAISS et GIT (pour CLIP)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie de tout le code du backend
COPY ./app ./app
EXPOSE 8000

# Lancement de l'API
CMD python app/init_db.py && uvicorn app.main:app --host 0.0.0.0 --port 8000
