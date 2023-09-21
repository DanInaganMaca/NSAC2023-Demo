# NSAC2023-Demo
Demo

- Instalar Virtual Box
- Crear Maquina Virtual Ubuntu

----
# Pasos para conectar a GitHub a través de SSH

1. Genera una nueva clave SSH en tu máquina local, si aún no tienes una. Puedes usar el siguiente comando en tu terminal:
   ```
   ssh-keygen -t rsa -b 4096 -C "tu_email@example.com"
   ```

2. Sigue las instrucciones para guardar la clave en la ubicación predeterminada (`~/.ssh/id_rsa`) o elige una ruta personalizada.

3. Abre el archivo de clave pública para copiar su contenido. Puedes usar el siguiente comando para abrir el archivo en el terminal:
   ```
   cat ~/.ssh/id_rsa.pub
   ```

4. Copia la salida completa del comando anterior.

5. Inicia sesión en tu cuenta de GitHub y haz clic en tu foto de perfil en la esquina superior derecha de la pantalla. Luego, selecciona "Settings" en el menú desplegable.

6. En la barra lateral izquierda, haz clic en "SSH and GPG keys".

7. Haz clic en "New SSH key" o "Add SSH key".

8. Proporciona un título descriptivo para tu clave SSH en el campo "Title".

9. Pega tu clave pública en el campo "Key".

10. Haz clic en "Add SSH key" para guardar y agregar la clave a tu cuenta de GitHub.

¡Eso es todo! Ahora has conectado con éxito GitHub a través de SSH. Puedes probar la conexión usando el siguiente comando en la terminal:
```
ssh -T git@github.com
```

# Pasos para instalar Docker en Linux

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

- clonar repositorio 
  . git clone https://github.com/DanInaganMaca/NSAC2023-Demo.git 
