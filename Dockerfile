# Usa una imagen base oficial de AWS para Python en Lambda
FROM public.ecr.aws/lambda/python:3.12

# Copia el archivo de requerimientos
COPY requirements.txt ./

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de tu proyecto a la imagen
# (Aquí es donde el .dockerignore hace su magia, excluyendo lo que no se necesita)
COPY . .

# Expone el puerto que usa FastAPI (buena práctica)
EXPOSE 8000

# El comando que Lambda usará para iniciar tu aplicación
CMD ["main.app"]