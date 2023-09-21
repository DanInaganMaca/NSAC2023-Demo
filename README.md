# NSAC2023-Demo
Demo

- Instalar Virtual Box
- Crear Maquina Virtual Ubuntu

==========

1. Instalar SSH en caso de que no lo tenga
```bash
sudo apt-get install openssh-server
```

3. Instalar git
```bash
sudo apt-get install git
```
  
4. Instalar docker
```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
```
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
```bash
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
```bash
sudo apt-get update
```
```bash
sudo apt-get upgrade
```
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io
```
```bash
sudo systemctl status docker
```
```bash
sudo usermod -aG docker $USER
```
- Probar si Docker funciona
```bash
docker run hello-world
```
```bash
docker run -it ubuntu bash
```

4. clonar repositorio
```bash
git clone https://github.com/DanInaganMaca/NSAC2023-Demo.git
```
