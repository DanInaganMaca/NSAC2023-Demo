# Ambiente de desarrollo para el proyecto NSAC2023-Demo

Antes de comenzar a instalar el ambiente de desarrollo, es importante realizar algunas tareas previas. Estas tareas incluyen establecer la conexión de GitHub a través de SSH, así como instalar Docker, nvm y Python 3.

La conexión de GitHub a través de SSH permite una comunicación segura entre tu máquina local y el servidor de GitHub. Esto es necesario para clonar y gestionar el repositorio de manera segura.

Docker es una plataforma que simplifica el proceso de configuración y ejecución de aplicaciones en contenedores. Proporciona un ambiente consistente y aislado para el desarrollo y despliegue de aplicaciones.

nvm, o Node Version Manager, es una herramienta que facilita la instalación y gestión de múltiples versiones de Node.js en tu máquina. Esto es útil si necesitas trabajar con diferentes versiones de Node.js en diferentes proyectos.

Python 3 es un lenguaje de programación ampliamente utilizado y es necesario instalarlo para ejecutar ciertas aplicaciones y herramientas en el ambiente de desarrollo.

Realizar estas tareas previas garantizará que tu ambiente de desarrollo esté configurado correctamente y pueda funcionar de manera óptima. Asegúrate de seguir la guía a continuación adecuadamente para establecer la conexión de GitHub a través de SSH, instalar Docker, nvm y Python 3 antes de continuar con la instalación del ambiente de desarrollo.

1. [Establecer conexión con GitHub a través de SSH](#establecer-conexión-con-github-a-través-de-ssh)  
1.1 [Clonar repositorio como Developer](#clonar-repositorio-como-developer)
2. [Instalar Docker en Linux](#instalar-docker-en-linux)
3. [Instalar nvm y gestionar versiones de Node.js](#instalar-nvm-y-gestionar-versiones-de-nodejs)  
3.1 [Instalación de nvm](#instalación-de-nvm)  
3.2 [Uso del archivo .nvmrc](#uso-del-archivo-nvmrcy)
4. [Instalar Python 3](#instalar-python-3)

Las siguientes herramientas también deben estar instaladas en el sistema operativo: `git` y `ssh`. El comando para instalarlo es el siguiente:

```
sudo apt install git openssh-server
```

----
## Establecer conexión con GitHub a través de SSH

   ```
   cd
   cd .ssh/
   ```

1. Genera una nueva clave SSH en tu máquina local, si aún no tienes una. Puedes usar el siguiente comando en tu terminal:
   ```
   ssh-keygen -t ed25519 -b 4096 -C "{yourusername@emaildomain.com}" -f {ssh-key-name}
   ```
   {username@emaildomain.com} is the email address associated with the Bitbucket Cloud account, such as your work email account.
   {ssh-key-name} is the output filename for the keys. We recommend using a identifiable name such as bitbucket_work.

2. Agrega una contraseña. 

3. Add the ssh key to your local and copy the .pud
   ```
   ssh-add {ssh-key-name}
   ```
   ```
   cat {ssh-key-name}.pub
   ```
5. Copia la salida completa del comando anterior.

6. Inicia sesión en tu cuenta de GitHub y haz clic en tu foto de perfil en la esquina superior derecha de la pantalla. Luego, selecciona "Settings" en el menú desplegable.

7. En la barra lateral izquierda, haz clic en "SSH and GPG keys".

8. Haz clic en "New SSH key" o "Add SSH key".

9. Proporciona un título descriptivo para tu clave SSH en el campo "Title".

10. Pega tu clave pública en el campo "Key".

11. Haz clic en "Add SSH key" para guardar y agregar la clave a tu cuenta de GitHub.

¡Eso es todo! Ahora has conectado con éxito GitHub a través de SSH. Puedes probar la conexión usando el siguiente comando en la terminal:
```
ssh -T git@github.com
```

### Clonar repositorio como Developer

Ya que se ha establecido la conexión con GitHub a través de SSH, puedes proceder a clonar el repositorio para colaborar en el desarrollo con los siguientes pasos:

1. Abre tu terminal o línea de comandos.

2. Navega hasta el directorio donde deseas clonar el repositorio usando el comando `cd [directorio]`. Por ejemplo, si deseas clonar el repositorio en el directorio "Documentos", ingresa `cd Documentos`.

3. Una vez en el directorio adecuado, utiliza el siguiente comando para clonar el repositorio:

```
git clone git@github.com:DanInaganMaca/NSAC2023-Demo.git
```

4. Presiona Enter para ejecutar el comando. Esto creará una copia local del repositorio en tu directorio actual.

¡Y eso es todo! Ahora has clonado el repositorio del ambiente de desarrollo como desarrollador en GitHub.

**Nota:** si se va a visualizar el repositorio como no colaborador/developer utilizar el siguiente comando:

```
git clone https://github.com/DanInaganMaca/NSAC2023-Demo.git
```


## Instalar Docker en Linux

1. Actualiza los paquetes existentes en tu sistema ejecutando el siguiente comando en la terminal:
   ```
   sudo apt update
   ```

2. Instala los paquetes necesarios para permitir que apt utilice repositorios a través de HTTPS:
   ```
   sudo apt install apt-transport-https ca-certificates curl software-properties-common
   ```

3. Descarga e importa la clave GPG oficial de Docker ejecutando el siguiente comando en la terminal:
   ```
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```

4. Añade el repositorio de Docker a las fuentes de apt ejecutando el siguiente comando:
   ```
   echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

5. Actualiza los paquetes nuevamente para incluir el repositorio de Docker:
   ```
   sudo apt update
   ```

6. Instala Docker usando el siguiente comando:
   ```
   sudo apt install docker-ce docker-ce-cli containerd.io
   ```

7. Verifica si Docker se ha instalado correctamente ejecutando el siguiente comando:
   ```
   docker --version
   ```

8. Para permitir que tu usuario ejecute comandos Docker sin usar `sudo`, añade tu usuario al grupo `docker` ejecutando el siguiente comando:
   ```
   sudo usermod -aG docker $USER
   ```

9. Cierra la sesión actual o reinicia tu máquina para aplicar los cambios.

## Instalar nvm y gestionar versiones de Node.js

Este es un tutorial para ayudarte a instalar nvm (Node Version Manager) en tu sistema y utilizar el archivo .nvmrc para especificar y gestionar la versión de Node.js necesaria del proyecto.

### Instalación de nvm

1. Abre tu terminal y ejecuta el siguiente comando para descargar e instalar el script de instalación de nvm:

   ```
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
   ```

2. Una vez que la instalación se complete, cierra y vuelve a abrir la terminal o ejecuta el siguiente comando para cargar nvm en tu sesión actual:

   ```
   source ~/.bashrc
   ```

   Si estás usando bash como tu shell, puedes usar también el archivo `~/.bash_profile` en lugar de `~/.bashrc`.

3. Verifica que nvm se haya instalado correctamente ejecutando el siguiente comando:

   ```
   nvm --version
   ```

   Deberías ver el número de versión de nvm si la instalación fue exitosa.

### Uso del archivo .nvmrc

El archivo .nvmrc permite especificar una versión específica de Node.js para utilizar en un proyecto determinado. Sigue estos pasos para utilizarlo:

1. Dirígete al directorio del ambiente de frontend de React, el cual se encuentra en la siguiente ruta:

```
  cd ./docker-NSAC2023-demo/react_app
```

2. Ejecuta el siguiente comando para dejar que nvm seleccione y establezca la versión específica de Node.js:

   ```
   nvm install
   ```

   nvm leerá el archivo .nvmrc y descargará e instalará automáticamente la versión especificada de Node.js si aún no está instalada en tu sistema.

3. Una vez que se complete la instalación, nvm habrá configurado la versión de Node.js especificada en el archivo .nvmrc. Puedes verificarlo ejecutando el siguiente comando:

   ```
   node --version
   ```

   Deberías ver que la versión de Node.js sea la misma que especifica el archivo .nvmrc.

¡Y eso es todo! Ahora estás utilizando la versión de Node.js específica para el proyecto a través del archivo .nvmrc.

## Instalar Python 3

Para instalar Python 3, en la terminal, ejecuta el siguiente comando:

```
  sudo apt install python3 python3-pip
```

El sistema te pedirá que confirmes la instalación y te mostrará el espacio en disco que se utilizará. Si estás de acuerdo, presiona "y" y luego "Enter" para comenzar la instalación.

Una vez que la instalación finalice, podrás verificar la versión de Python 3 ejecutando el siguiente comando:

```
 python3 --version
```

Debería mostrarse la versión instalada de Python 3.

¡Y eso es todo! Has instalado Python 3 en tu sistema.

---

## Install Conda

1. Download the latest Miniconda installer script for 64-bit Linux using wget: ```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

2. Make the installer script executable:
```
chmod +x Miniconda3-latest-Linux-x86_64.sh
```

3. Run the Miniconda installer script:
```
./Miniconda3-latest-Linux-x86_64.sh
```
Follow the on-screen instructions to complete the installation. You'll be prompted to review the license agreement (press ENTER to scroll through), accept the terms by typing yes, and choose the installation location (the default is usually fine).

4. After the installation is complete, you'll be asked if you want to initialize Miniconda. It's recommended to answer 'yes' to this option. This will add Conda to your shell configuration, allowing you to use it in your terminal.

5. To activate the changes in your current terminal session, use:
```
source ~/.bashrc
```

6. Verify that Conda has been successfully installed by checking the version:
```
conda --version
```

--- 

## Continua con la guía para ejecutar el ambiente de desarrollo

Una vez que todas las herramientas necesarias se encuentran instaladas en tu sistema, es momento de ejecutar el ambiente de desarrollo. Los pasos para ejecutar el ambiente se encuentran en la siguiente guía: 

[Ejecutar ambiente de desarrollo](/docker-NSAC2023-demo/README.md)
