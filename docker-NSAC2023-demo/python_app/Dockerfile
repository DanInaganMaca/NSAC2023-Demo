FROM ubuntu:22.04

RUN apt-get update \
    && apt-get install -y python3-dev python3-pip build-essential libssl-dev libffi-dev libc6-dev

WORKDIR /app

# Copiamos los archivos de la aplicación
COPY ./requirements.txt ./
COPY ./ ./

# Instalamos las dependencias
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
