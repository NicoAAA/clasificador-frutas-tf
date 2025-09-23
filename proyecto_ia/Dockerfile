# Usa la imagen base oficial de AWS para Python 3.10. Esto es el cambio clave.
FROM public.ecr.aws/lambda/python:3.10

# Establece el directorio de trabajo dentro del contenedor.
WORKDIR /app

# Copia primero el archivo de dependencias para aprovechar el caché de Docker.
COPY requirements.txt .

# Instala las dependencias.
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copia todo el código de tu aplicación al directorio de trabajo.
COPY . .

# Comando que AWS Lambda usará para iniciar la aplicación.
# En el contexto de la imagen base de AWS, este comando SÍ funciona correctamente.
CMD ["main.handler"]