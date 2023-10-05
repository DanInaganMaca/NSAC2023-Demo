# Usar una imagen base con Conda y Python
FROM continuumio/miniconda3:4.9.2

WORKDIR /app

# Copiar el código fuente del proyecto al contenedor
COPY python_app/ ./

# Crear y activar un entorno Conda
RUN echo "source activate ./venv" > ~/.bashrc
ENV PATH /app/venv/bin:$PATH

# Configurar y ejecutar Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
