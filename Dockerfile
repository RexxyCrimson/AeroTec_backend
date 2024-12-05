# Usa una imagen base de Python
FROM python:3.11

# Define el directorio de trabajo
WORKDIR /app

# Copia los requerimientos
COPY requirements.txt /app/

# Instala las dependencias con las versiones requeridas
RUN pip install -r requirements.txt

# Copia el proyecto al contenedor
COPY . /app/

# Expone el puerto para la aplicación
EXPOSE 8000