# Ejecutar ambiente de desarrollo

1. [Instalar dependencias de React](#instalar-dependencias-de-react)
2. [Instalar dependencias de Python](#instalar-dependencias-de-python)
3. [Ejecutar Docker compose](#ejecutar-docker-compose)
4. [Pruebas de funcionamiento](#pruebas-de-funcionamiento)  
4.1 [Comunicación entre Backend Django y DB Postgresql](#comunicación-entre-backend-django-y-db-postgresql)
5. [Solución de problemas](#solución-de-problemas)

---

## Instalar dependencias de React

1. Navega hasta el directorio del proyecto de React del repositorio, es el directorio llamado `react_app`.
   
2. Utiliza nvm para obtener la versión de Node.js necesaria para el proyecto:

   ```
   cd
   cd Documents/
   cd NSAC2023-Demo/docker-NSAC2023-demo/react_app/
   ```
   ```
   nvm use
   ```

   Si obtienes la versión correspondiente, puedes pasar al siguiente paso. Si no, vuelve a la guía del ambiente de desarrollo.

4. Una vez en el directorio raíz del repositorio clonado, busca el archivo `package.json`. Este archivo es esencial para instalar las dependencias del proyecto.

5. En la terminal, ejecuta el siguiente comando para instalar todas las dependencias del proyecto listadas en el archivo `package.json` y resolver los problemas relacionados con las dependencias heredadas:

   ```
   npm i --legacy-peer-deps
   ```

   Este comando leerá el archivo `package.json`, descargará e instalará todas las dependencias necesarias, y a su vez resolverá cualquier problema relacionado con las dependencias heredadas.

6. Una vez que el comando `npm i --legacy-peer-deps` haya terminado de ejecutarse, todas las dependencias del proyecto deberían estar instaladas y listas para usar.

Recuerda que el uso de `--legacy-peer-deps` puede ser necesario si estás utilizando una versión de npm anterior a la 7. Si estás utilizando npm 7 o superior, este flag no será necesario.

El archivo `package.json` es una referencia para las dependencias del proyecto, por lo que es importante mantenerlo actualizado según las necesidades del proyecto. Si se agregan o eliminan dependencias, debes ejecutar nuevamente el comando `npm i --legacy-peer-deps` para tener las dependencias actualizadas.

¡Y eso es todo! Has instalado las dependencias del ambiente frontend.

## Instalar dependencias de Python

1. Navega hasta el directorio del proyecto de Python, es el directorio llamado `python_app`.

2. Para gestionar las dependencias de Python, es recomendable utilizar un entorno virtual. Esto te permite aislar las dependencias del proyecto del resto del sistema. Si no tienes instalado `virtualenv`, puedes instalarlo ejecutando el siguiente comando:

   ```
   cd
   cd Documents/
   cd NSAC2023-Demo/docker-NSAC2023-demo/python_app/
   ```
   ```
   sudo apt install python3-virtualenv
   ```

3. Crea el archivo '.env': ejecuta el comando `nano .env` y guarda ahí lo siguiente:
   ```
   nano .env
   ```
   Copy in that file the next and save
   ```
   # .env

   DEBUG=True
   SECRET_KEY=secret
   DB_NAME=nsac2023-demo
   DB_USER=root
   DB_PASSWORD=secret
   DB_HOST=db
   DB_PORT=5432
   ```
   Verify this with:
   ```
   cat .env
   ```
   
4. Una vez instalado `virtualenv`, crea un nuevo entorno virtual ejecutando el siguiente comando en la terminal:

   ```
   virtualenv venv
   ```

   Esto creará un nuevo directorio llamado "env" que contendrá el entorno virtual.

5. Activa el entorno virtual ejecutando el siguiente comando:

     ```
     source venv/bin/activate
     ```

   Al activar el entorno virtual, el prompt de la terminal debe cambiar para indicar que estás utilizando el entorno virtual.

6. Una vez dentro del entorno virtual, puedes instalar las dependencias del proyecto utilizando el gestor de paquetes `pip`. En el directorio raíz del proyecto, normalmente se encuentra un archivo `requirements.txt` que lista todas las dependencias necesarias.

   Ejecuta el siguiente comando para instalar todas las dependencias del proyecto:

   ```
   pip install -r requirements.txt
   ```
   ```
   exit
   ```

   Esto leerá el archivo `requirements.txt` y descargará e instalará todas las dependencias necesarias en el entorno virtual.

7. Una vez que todas las dependencias se hayan instalado correctamente, estamos listos para ejecutar los contenedores.

Y eso es todo. Ahora has instalado las dependencias del ambiente backend.

## Install Conda Dependences 

   ```
   cd
   cd Documents/
   cd NSAC2023-Demo/docker-NSAC2023-demo/python_app/
   ```
1. Create a conda virtual environment
   ```
   conda env create -p ./venv -f environment.yml
   ```
   
2. Activate conda environment
   ```
   cat env   
   ```
4. Install the dependences 
   ```
   conda env update -f environment.yml
   ```

## Ejecutar Docker compose

1. Asegúrate de tener Docker y Docker Compose instalados en tu sistema. Puedes verificarlo ejecutando los siguientes comandos en la terminal:
   ```
   cd
   cd Documents/
   cd NSAC2023-Demo/docker-NSAC2023-demo/
   ```
   ```
   docker --version
   ```

   Si obtienes las versiones correspondientes, puedes pasar al siguiente paso. Si no, vuelve a la guía del ambiente de desarrollo.

2. Navega hasta el directorio donde se encuentra el archivo `docker-compose.yml`, se encuentra en el directorio `docker-NSAC2023-demo`. Este archivo es esencial para describir y configurar los servicios que serán ejecutados dentro de los contenedores de Docker.

3. Antes de ejecutar los contenedores, es necesario construir las imágenes Docker si aún no están construidas. Para ello, ejecuta el siguiente comando en la terminal:

   ```
   docker compose build
   ```

   Esto leerá el archivo `docker-compose.yml` y construirá las imágenes Docker necesarias para los servicios especificados en el archivo. Este paso es necesario solo en la primera ejecución o cuando se realicen cambios en las imágenes o en los archivos de construcción.

4. Una vez que las imágenes están construidas, puedes ejecutar los contenedores utilizando el siguiente comando en la terminal:

   ```
   docker compose up
   ```

   Este comando leerá el archivo `docker-compose.yml` y comenzará a crear y ejecutar los contenedores de cada servicio especificado en el archivo. Verás la salida de registro de cada contenedor en la terminal.

   Si deseas ejecutar los contenedores en segundo plano (detached mode), puedes agregar la bandera `-d` al comando:

   ```
   docker compose up -d
   ```

5. Una vez que todos los contenedores estén en funcionamiento, tendrás acceso a los servicios definidos en `docker-compose.yml`.

**Recomendación:** Recomiendo que después de ejecutar los contenedores y si fue a través del comando para ejecutar en segundo plano tener presente el siguiente comando para observar el registro de los servicios de la aplicación:

```
  docker compose logs -f
```

  Para salir de la vista de logs pulsa `Ctrl+c`.

6. Para detener y eliminar los contenedores, puedes ejecutar el siguiente comando en la misma terminal:

   ```
   docker compose down
   ```

   Esto detendrá y eliminará todos los contenedores creados por `docker-compose`.

Recuerda que debes ejecutar el comando `docker-compose build` la primera vez que ejecutes los contenedores o cada vez que realices cambios en las imágenes o en los archivos de construcción, y luego puedes utilizar `docker-compose up` para iniciar los contenedores.

¡Y eso es todo! Has ejecutado `docker-compose` correctamente, construido los contenedores cuando es necesario y estás utilizando los servicios definidos en el archivo `docker-compose.yml`.

## Pruebas de funcionamiento

En esta sección se registran todas las pruebas de funcionamiento para saber si el ambiente de desarrollo quedo instalado correctamente.

### Comunicación entre Backend Django y DB Postgresql

Para verificar que el ambiente de backend con Django ha establecido la conexión correctamente con la base de datos Postgresql en el contenedor de Docker, se puede realizar las siguientes pruebas de funcionamiento. 

#### Verificar la Migración de la base de datos
Asegurar que las migraciones de Django se hayan aplicado correctamente. Es importante haber ejecutado el comando para aplicar migraciones, así aplicará las migraciones pendientes y creará las tablas necesarias en la base de datos.
```
  docker compose exec python /app/venv/bin/python manage.py migrate
```
```
  docker compose exec python /app/venv/bin/python manage.py makemigrations
```
#### Crear un Superusuario

Crea un superusuario de Django para poder acceder al panel de administración y realizar pruebas. Ejecuta el siguiente comando y sigue las instrucciones:

```
  docker-compose exec python /app/venv/bin/python manage.py createsuperuser
```

Luego, abre un navegador web y accede al panel de administración de Django ingresando la dirección http://localhost:8000/admin/. Inicia sesión con el superusuario que creaste. Si puedes iniciar sesión y ver el panel de administración, significa que la conexión a la base de datos funciona correctamente.

**Verificar el registro en la Base de Datos:** Puedes verificar el registro de datos directamente en la base de datos PostgreSQL. Para hacerlo, puedes usar una herramienta de administración de bases de datos como pgAdmin, DBeaver o conectarte a la base de datos desde la línea de comandos en el contenedor de Python utilizando psql. Por ejemplo:

```
  docker-compose exec db psql -U root -d nsac2023-demo

```

## Solución de problemas

En esta sección se registran las soluciones a los problemas que se presentan al momento de ejecutar la construcción de las imágenes de los contenedores y cuando se están ejecutando los contenedores.

* Proteger la información sensible de la base de datos en un proyecto es una práctica importante para mantener la seguridad de los datos. Por ello, al ejecutar los contenedores con el comando `docker compose up` lanza una excepción en el contenedor `python-container`, el cual es sobre una conexión rehusada. Para resolverlo se debe crear un archivo dentro del directorio `python_app` llamado `.env` allí poner las credenciales de la base de datos. Dichas credenciales solicitarlas por interno. 

* Cuando se presentan problemas al construir, iniciar o ejecutar los contenedores y estos están relacionados directamente con el contenedor `python-container`, es esencial ejecutar el comando de migración de modelos de Django, ya que al hacer modificaciones de modelo, crear modelos, instalar dependencias o cualquier otra operación se lanzaran errores inesperados. Por lo tanto, para resolver esto se suele usar el comando `python manage.py migration`, pero como estamos usando un contenedor el comando es: 

```
  docker compose exec python /app/venv/bin/python manage.py migrate 
```
