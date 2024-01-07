# Deployment-and-Monitoring-Pacmann---Deploy-Web-App
the purpose of this project is to deploy previous web architecture project, twittr app that is. it can be accesed in https://github.com/frhnkl/Web-Arc-twttr-app. The twittr app  was made using vue for front-end and flask for backend. In the project, we will try to deploy it so it can be accessed through website alongside with integrating CI/CD pipeline for this project.
## Workflow
## Server Preparation
- Installing docker
  docker is free and supports various OS. it can be downloaded in https://docs.docker.com/desktop/
- Installing Ubuntu and Nginx
  depending on your OS, there are various way to install Ubuntu and nginx. For windows, please follow this instruction
  1. Step 1: Install WSL.
  In the Windows Search bar, type “turn Windows features on or off” and then open the corresponding app.
  Scroll down to check the boxes in front of Virtual Machine Platform and Windows Subsystem for Linux. Then, click OK.
  2. Install ubuntu
     open windows powershell and copy this line
      ```
     wsl --install -d ubuntu
      ```
  3. Install Nginx
     after installing Ubuntu, you can install ngingx using
     ```
     sudo apt update
     sudo apt install nginx
     ```

- Firewall Configuration
  firewall configuration can also be done in nginx by typing
  ```
  sudo ufw app list
  ```
  You should get a listing of the application profiles:
  ```
  Nginx Full
  Nginx HTTP
  Nginx HTTPS
  OpenSSH
  ```
  since we are using port 80 for unencrypted traffic and port 443 for ecnrypted traffic, we should choose Nginx Full by typing
  ```
  sudo ufw allow 'Nginx Full'
  ```
  
  
## Preparing WebApp
## Setting up Docker
## CI/CD Workflow
## Web Server Config
## Domain and SSL
