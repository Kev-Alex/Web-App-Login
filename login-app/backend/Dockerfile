FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

# Instala dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential && rm -rf /var/lib/apt/lists/*

# Copia requirements e instala dependencias de Python
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente
COPY app ./app
COPY config.py ./config.py

# Configura PYTHONPATH (debe ir ANTES del CMD)
ENV PYTHONPATH=/app

EXPOSE 8081

# Comando para lanzar el servidor FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]

