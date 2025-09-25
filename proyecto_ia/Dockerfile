# Usa una imagen base de Python delgada. No necesitas la de AWS Lambda.
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia e instala los requerimientos
COPY requirements.txt .
# Agrega gunicorn a tus requerimientos
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de tu código
COPY . .

# Expone el puerto que usará tu aplicación
EXPOSE 8000

# ¡Este es el cambio clave!
# Inicia el servidor Gunicorn. Cloud Run inyectará la variable $PORT.
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]