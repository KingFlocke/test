# lab07/Dockerfile - Bauplan fuer das Image des Dienstes
# Bauen (aus dem Hauptordner des Repos):  docker build -t traeger-service -f lab07/Dockerfile .

# Grundsystem: schlankes Debian mit Python 3.12
FROM python:3.12-slim
# Arbeitsordner im Image - alle folgenden Pfade beziehen sich darauf
WORKDIR /app

# PyTorch als CPU-Variante (das Standardpaket bringt unter Linux die CUDA-Bibliotheken mit und ist um ein Vielfaches groesser)
RUN pip install --no-cache-dir torch==2.8.0 torchvision==0.23.0 \
    --index-url https://download.pytorch.org/whl/cpu

# Die uebrigen Pakete: erst nur die Liste kopieren, dann installieren
COPY lab07/requirements-service.txt .
RUN pip install --no-cache-dir -r requirements-service.txt

# Code, Modellbeschreibung und Modell - erst jetzt, NACH den Paketen
# TODO 3.2a (Loesung): vier COPY-Zeilen: lab02/src, lab07/app.py, models/traeger_v1.yaml, lab07/model (jeweils gleicher Pfad im Image)
COPY lab02/src lab02/src
COPY lab07/app.py lab07/app.py
COPY models/traeger_v1.yaml models/traeger_v1.yaml
COPY lab07/model lab07/model

# Der Dienst laedt im Container aus dem Ordner statt ueber den Alias
ENV MODEL_URI=lab07/model
EXPOSE 8000
# TODO 3.2b (Loesung): CMD als Liste: uvicorn startet lab07.app:app mit --host 0.0.0.0 und --port 8000
CMD ["uvicorn", "lab07.app:app", "--host", "0.0.0.0", "--port", "8000"]
