FROM python:3.11-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar los archivos del proyecto a la imagen
COPY . .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 5000
EXPOSE 5000

# Comando por defecto para ejecutar la aplicación
CMD ["waitress-serve", "--port=5000", "app:app"]