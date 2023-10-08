# Part I: Development environment for the NSAC2023-Demo project


Before starting to install the development environment, it is important to perform some preliminary tasks. These tasks include establishing the GitHub connection via SSH, as well as installing Docker, nvm, and Python 3.

Connecting to GitHub via SSH allows secure communication between your local machine and the GitHub server. This is necessary to clone and manage the repository securely.

Docker is a platform that simplifies the process of setting up and running containerized applications. Provides a consistent and isolated environment for application development and deployment.

nvm, or Node Version Manager, is a tool that makes it easy to install and manage multiple versions of Node.js on your machine. This is useful if you need to work with different versions of Node.js in different projects.

Python 3 is a widely used programming language and is required to be installed to run certain applications and tools in the development environment.

Performing these preliminary tasks will ensure that your development environment is configured correctly and can function optimally. Make sure you follow the guide below properly to establish the GitHub connection via SSH, install Docker, nvm, and Python 3 before proceeding with the installation of the development environment.

1. [Establish connection to GitHub via SSH](#establish-connection-to-github-via-ssh)
1.1 [Clone repository as Developer](#clone-repository-as-developer)
2. [Install Docker on Linux](#install-docker-on-linux)
3. [Install nvm and manage Node.js versions](#install-nvm-and-manage-nodejs-versions)
3.1 [nvm installation](#nvm-installation)
3.2 [Use of .nvmrc file](#use-of-nvmrcy-file)
4. [Install Python 3](#install-python-3)

## Install GNU Linux Ubuntu in a Virtual Machine 

You can see this tutorial to install Ubuntu in a Virtual Machine

(YouTube Tutorial)[https://www.youtube.com/watch?v=rJ9ysibH768]

## Install Git and SSH 

The following tools must also be installed on the operating system: `git` and `ssh`. The command to install it is the following:

```
sudo apt-get update
sudo apt-get upgrade -y
```

```
sudo apt install git openssh-server
```

----
## Establish connection to GitHub via SSH 
{{ ¡¡ This step is only necessary for developers/collaborators of the project !! }} 

   ```
   cd
   cd .ssh/
   ```

1. Generate a new SSH key on your local machine, if you don't already have one. You can use the following command in your terminal:
   ```
   ssh-keygen -t ed25519 -b 4096 -C "{yourusername@emaildomain.com}" -f {ssh-key-name}
   ```
   {username@emaildomain.com} is the email address associated with the GitHUb Cloud account, such as your work email account.
   {ssh-key-name} is the output filename for the keys. We recommend using a identifiable name such as 'ssh-key-nsac2023'.

2. Add a password and remember it. 

3. Add the ssh key to your local and copy the .pub
   ```
   ssh-add {ssh-key-name}
   ```
   ```
   cat {ssh-key-name}.pub
   ```
5. Copy the complete output of the previous command.

6. Sign in to your GitHub account and click your profile photo in the top right corner of the screen. Then, select “Settings” from the drop-down menu.

7. In the left sidebar, click "SSH and GPG keys."

8. Click "New SSH key" or "Add SSH key".

9. Provide a descriptive title for your SSH key in the "Title" field.

10. Paste your public key into the "Key" field.

11. Click "Add SSH key" to save and add the key to your GitHub account.

That's all! You have now successfully connected GitHub via SSH. You can test the connection using the following command in the terminal:

```
ssh -T git@github.com
```

## Clone repository

Clone the repository to the 'Documents' folder: 

```
cd
cd Documents/
```
```
git clone https://github.com/DanInaganMaca/NSAC2023-Demo.git
```

Or only for collaborators/developers: 

```
cd
cd Documents/
```
```
git clone git@github.com:DanInaganMaca/NSAC2023-Demo.git
```


## Install Docker on Linux

1. Update the existing packages on your system by running the following command in the terminal:

   ```
      sudo apt-get update
      sudo apt-get upgrade -y
   ```

2. Install the necessary packages to allow apt to use repositories over HTTPS:
   ```
   sudo apt install apt-transport-https ca-certificates curl software-properties-common
   ```

3. Download and import the official Docker GPG key by running the following command in the terminal:
   ```
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```

4. Add the Docker repository to the apt sources by running the following command:
   ```
   echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

5. Update the packages again to include the Docker repository:
   ```
      sudo apt-get update
      sudo apt-get upgrade -y
   ```

6. Install Docker using the following command:
   ```
   sudo apt install docker-ce docker-ce-cli containerd.io
   ```

7. Check if Docker has been installed correctly by running the following command:
   ```
   docker --version
   ```

8. To allow your user to run Docker commands without using `sudo`, add your user to the `docker` group by running the following command:
   ```
   sudo usermod -aG docker $USER
   ```

9. Log out of the current session or restart your machine to apply the changes.

## Install nvm and manage Node.js versions

This is a tutorial to help you install nvm (Node Version Manager) on your system and use the .nvmrc file to specify and manage the Node.js version required for your project.

### Instalación de nvm

1. Open your terminal and run the following command to download and install the nvm installation script:

   ```
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
   ```

2. Once the installation is complete, close and reopen the terminal or run the following command to load nvm into your current session:

   ```
   source ~/.bashrc
   ```

If you are using bash as your shell, you can also use the `~/.bash_profile` file instead of `~/.bashrc`.

3. Verify that nvm has been installed correctly by running the following command:

   ```
   nvm --version
   ```
   
You should see the nvm version number if the installation was successful.


### Using the .nvmrc file

The .nvmrc file allows you to specify a specific version of Node.js to use for a given project. Follow these steps to use it:

1. Go to the React frontend environment directory, which is located at the following path:

```
   cd
   cd Documents/
   cd NSAC2023-Demo/docker-NSAC2023-demo/react_app/
```

2. Run the following command to let nvm select and set the specific Node.js version:

   ```
   nvm install
   ```

nvm will read the .nvmrc file and automatically download and install the specified version of Node.js if it is not already installed on your system.

3. Once the installation is complete, nvm will have configured the version of Node.js specified in the .nvmrc file. You can verify it by running the following command:

   ```
   node --version
   ```

You should see that the Node.js version is the same as what the .nvmrc file specifies.

And that's it! You are now using the project-specific version of Node.js via the .nvmrc file.

## Install Python 3

To install Python 3, in the terminal, run the following command:

```
  sudo apt install python3 python3-pip
```

The system will ask you to confirm the installation and show you the disk space that will be used. If you agree, press "y" and then "Enter" to begin the installation.

Once the installation is complete, you can check the Python 3 version by running the following command:

```
 python3 --version
```

The installed version of Python 3 should be displayed.

And that's it! You have installed Python 3 on your system.

---

## Install Conda

1. Download the latest Miniconda installer script for 64-bit Linux using wget:
   ```
      cd
      cd Downloads/ 
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

# Part II: 
## Continue with the guide to run the development environment

Once all the necessary tools are installed on your system, it is time to run the development environment. The steps to run the environment are found in the following guide:

[Run development environment](/docker-NSAC2023-demo/README.md)
