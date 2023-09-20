# NSAC2023-Demo
Demo

- Instalar Virtual Box
- Crear Maquina Virtual Ubuntu

==========

- Instalar SSH en caso de que no lo tenga
  . sudo apt-get install openssh-server

- Instalar git
  . sudo apt-get install git
  
- Instalar docker
  . sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
  . curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
  . echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  . sudo apt-get update
  . sudo apt-get upgrade
  . sudo apt-get install docker-ce docker-ce-cli containerd.io
  . sudo systemctl status docker
  . sudo usermod -aG docker $USER

- clonar repositorio 
  . git clone https://github.com/DanInaganMaca/NSAC2023-Demo.git 
