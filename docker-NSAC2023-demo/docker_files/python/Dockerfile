FROM ubuntu:22.04

RUN apt-get update \
    && apt-get install -y python3-dev python3-pip virtualenv build-essential libssl-dev libffi-dev libc6-dev

WORKDIR /app

# Copiamos los archivos de la aplicación
COPY python_app/requirements.txt ./
COPY python_app/ ./

RUN alias python="/app/venv/bin/python"

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
