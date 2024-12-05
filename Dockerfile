# Usa una imagen base de Python
FROM python:3.11

# Define el directorio de trabajo
WORKDIR /app

# Copia los requerimientos
COPY requirements.txt /app/

# Instala las dependencias con las versiones requeridas
RUN pip install --no-cache-dir -r requirements.txt

# Instalar Gunicorn (asegúrate de incluirlo en requirements.txt o instálalo explícitamente aquí)
RUN pip install gunicorn

# Copia el proyecto al contenedor
COPY . /app/

# Expone el puerto para la aplicación
EXPOSE 8000

CMD ["gunicorn", "djangocrud.wsgi:application", "--bind", "0.0.0.0:8000"]