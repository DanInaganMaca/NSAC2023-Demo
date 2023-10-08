# Part II: Run development environment

1. [Install React Dependencies](#install-react-dependencies)
2. [Install Python dependencies](#install-python-dependencies)
3. [Run Docker compose](#run-docker-compose)
4. [Performance tests](#performance-tests)
4.1 [Communication between Backend Django and DB Postgresql](#communication-between-backend-django-and-db-postgresql)
5. [Troubleshooting](#troubleshooting)

---
## Install React dependencies

1. Navigate to the React project directory of the repository, it is the directory called `react_app`.
   ```
   cd
   cd Documents/
   cd NSAC2023-Demo/docker-NSAC2023-demo/react_app/
   ```
   
2. Use nvm to get the Node.js version needed for the project:
   ```
   nvm use
   ```

If you get the corresponding version, you can proceed to the next step. If not, return to the development environment guide.

4. Once in the root directory of the cloned repository, look for the `package.json` file. This file is essential to install the project dependencies.

5. In the terminal, run the following command to install all project dependencies listed in the `package.json` file and resolve issues related to inherited dependencies:
   ```
   npm i --legacy-peer-deps
   ```

This command will read the `package.json` file, download and install all necessary dependencies, and in turn resolve any issues related to inherited dependencies.

6. Once the `npm i --legacy-peer-deps` command has finished running, all project dependencies should be installed and ready to use.

Remember that using `--legacy-peer-deps` may be necessary if you are using a version of npm earlier than 7. If you are using npm 7 or higher, this flag will not be necessary.

The `package.json` file is a reference for the project's dependencies, so it is important to keep it updated according to the needs of the project. If dependencies are added or removed, you must run the `npm i --legacy-peer-deps` command again to have the dependencies updated.

And that's it! You have installed the frontend environment dependencies.

## Install Python dependencies

1. Navigate to the Python project directory, it is the directory called `python_app`.

   ```
   cd
   cd Documents/
   cd NSAC2023-Demo/docker-NSAC2023-demo/python_app/
   ```

2. To manage Python dependencies, it is recommended to use a virtual environment. This allows you to isolate the project's dependencies from the rest of the system. If you do not have `virtualenv` installed, you can install it by running the following command:
   ```
   sudo apt install python3-virtualenv
   ```

3. Create the '.env' file: run the command `nano .env` and save the following there:
   ```
   nano .env
   ```
   Copy in that file the next, and save
   ```
   #### .env 
   # PostgreSQL

   # Local DB 

   DEBUG=True
   SECRET_KEY=secret
   DB_NAME=nsac2023-demo
   DB_USER=root
   DB_PASSWORD=secret
   DB_HOST=db
   DB_PORT=5432

   # Remote DB - Supabase

   SUPABASE_DB=postgres
   SUPABASE_USER=postgres
   SUPABASE_HOST=db.cdbqpsbsmbndcmijyrkh.supabase.co
   SUPABASE_PW=Spectrum4Bio.2023
   ```
   Verify this with:
   ```
   cat .env
   ```
   
4. Once `virtualenv` is installed, create a new virtual environment by running the following command in the terminal:
   ```
   virtualenv venv
   ```

This will create a new directory called "env" that will contain the virtual environment.

5. Activate the virtual environment by running the following command:
     ```
     source venv/bin/activate
     ```

When you activate the virtual environment, the terminal prompt should change to indicate that you are using the virtual environment.

6. Once inside the virtual environment, you can install the project dependencies using the `pip` package manager. In the root directory of the project, there is usually a `requirements.txt` file that lists all the necessary dependencies.

    Run the following command to install all project dependencies:

   ```
   pip install -r requirements.txt
   ```
   ```
   exit
   ```

This will read the `requirements.txt` file and download and install all necessary dependencies into the virtual environment.

7. Once all the dependencies have been installed successfully, we are ready to run the containers.

And that's it. You have now installed the backend environment dependencies.

## Install Conda Dependencies
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
   conda activate ./venv
   ```
4. Install the dependences 
   ```
   conda env update -f environment.yml
   ```

5. Install python dependences

   ```
   pip install --no-cache-dir -r requirements.txt
   ```
In case a pip or python version error appears, use pip3 as follows: 
   ```
   pip3 install --no-cache-dir -r requirements.txt
   ```
And finally
   ```
   exit
   ```

## Run Docker compose

1. Make sure you have Docker and Docker Compose installed on your system. You can verify it by running the following commands in the terminal:
   ```
   cd
   cd Documents/
   cd NSAC2023-Demo/docker-NSAC2023-demo/
   ```
   ```
   docker --version
   ```

If you get the corresponding versions, you can proceed to the next step. If not, return to the development environment guide.

2. Navigate to the directory where the `docker-compose.yml` file is located, it is located in the `docker-NSAC2023-demo` directory. This file is essential to describe and configure the services that will be run inside Docker containers.

3. Before running the containers, you need to build the Docker images if they are not already built. To do this, run the following command in the terminal:

   ```
   docker compose build
   ```

This will read the `docker-compose.yml` file and build the necessary Docker images for the services specified in the file. This step is required only on the first run or when changes are made to images or build files.

4. Once the images are built, you can run the containers using the following command in the terminal:
   ```
   docker compose up
   ```

This command will read the `docker-compose.yml` file and start creating and running containers for each service specified in the file. You will see the log output of each container in the terminal.

    If you want to run the containers in the background (detached mode), you can add the `-d` flag to the command:
   ```
   docker compose up -d
   ```
5. Once all containers are up and running, you will have access to the services defined in `docker-compose.yml`.

**Recommendation:** I recommend that after running the containers and if it was through the command to run in the background, keep the following command in mind to observe the registration of the application services:

```
  docker compose logs -f
```

To exit the log view press `Ctrl+c`.

6. To stop and remove the containers, you can run the following command in the same terminal:
   ```
   docker compose down
   ```

This will stop and remove all containers created by `docker-compose`.

Remember to run the `docker-compose build` command the first time you run containers or each time you make changes to images or build files, and then you can use `docker-compose up` to start the containers.

And that's it! You have run `docker-compose` successfully, built containers when necessary, and are using the services defined in the `docker-compose.yml` file.

## Funcionality test

In this section all functional tests are recorded to know if the development environment was installed correctly.

### Communication between Django Backend and Postgresql DB

To verify that the Django backend environment has established the connection correctly with the Postgresql database in the Docker container, the following functional tests can be performed.

#### Verify Database Migration
Ensure that Django migrations have been applied correctly. It is important to have executed the command to apply migrations, so it will apply the pending migrations and create the necessary tables in the database.
```
  docker compose exec python /app/venv/bin/python manage.py makemigrations
```
```
  docker compose exec python /app/venv/bin/python manage.py migrate
```

#### Create a Super User

Create a Django superuser to be able to access the admin panel and run tests. Run the following command and follow the instructions:

```
  docker-compose exec python /app/venv/bin/python manage.py createsuperuser
```

Next, open a web browser and access the Django admin panel by entering the address http://localhost:8000/admin/. Sign in with the superuser you created. If you can log in and see the administration panel, it means that the database connection is working correctly.

**Verify the record in the Database:** You can verify the data record directly in the PostgreSQL database. To do this, you can use a database administration tool like pgAdmin, DBeaver or connect to the database from the command line in the Python container using psql. For example:

```
  docker-compose exec db psql -U root -d nsac2023-demo

```

## Troubleshooting

This section records solutions to problems that arise when building container images and when containers are running.

* Protecting sensitive database information in a project is an important practice to maintain data security. Therefore, when running the containers with the `docker compose up` command it throws an exception in the `python-container` container, which is about a refused connection. To solve it, you must create a file inside the `python_app` directory called `.env` and put the database credentials there. Request these credentials internally.

* When problems occur when building, starting or running containers and these are directly related to the `python-container` container, it is essential to run the Django model migration command, since when making model modifications, creating models, installing dependencies or any other operation will throw unexpected errors. Therefore, to solve this the command `python manage.py migration` is usually used, but since we are using a container the command is:
```
  docker compose exec python /app/venv/bin/python manage.py migrate 
```
