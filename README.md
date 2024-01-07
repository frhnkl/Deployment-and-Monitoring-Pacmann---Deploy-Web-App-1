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
- Dockerizing Flask-Backend
  to be autamatically run, we need to dockerize our backend by creating dockerfile with this
  ```
  FROM python:3.10.12-bullseye
  WORKDIR /app
  EXPOSE 5000
  # Installing pip
  COPY . /app
  RUN python -m pip install -r requirements.txt
  CMD ["python", "run.py"]
  ```
- Dockerizing Vue-Frontend
   to be autamatically run, we need to dockerize our backend by creating dockerfile with this
  ```
  FROM node:18
  WORKDIR /frontend
  COPY package*.json ./
  COPY .env ./
  RUN npm install
  COPY . .
  RUN npm run build
  EXPOSE 8080
  CMD ["npm", "run", "preview"]
  ```
## CI/CD Workflow
to be able to continuously pushing while deploying, we need to make great CI/CD pipeline to ensure that any change can be made and deployed continuously.
- for CI, we use yml like this. it ensuring build and test for docker thingies
```
name: CI (Continuous Integration)

on:
  pull_request:
    branches: [ "main" ]

jobs:

  build-testing:
    name: BuildnTest
    runs-on: windows-latest

    steps:
      - name: Check repository
        uses: actions/checkout@v2
    
      - name: Install Docker
        run: |
          sudo apt-get update
          sudo apt-get install -y docker-compose
      
      - name: BuildRun Container
        run: |
          sudo docker compose up -d

      - name: Requirements install
        run: |
          pip install -r testing\requirements.txt

      - name: Test
        run: |
          sleep 20
          pytest testing/test.py          
```
- for Continous Deployement (CD) we use this to make sure that build-push and deploy works well
  ```
      name: CI/CD

    on: workflow_dispatch
    
    jobs:
        
        build-push:
            name: Build and Push Image to Docker
            runs-on: windows-latest
    
            steps:
                - name: Check Repository
                  uses: actions/checkout@v2
    
                - name: Login Docker
                  uses: docker/login-action@v2
                  with:
                    username: ${{ secrets.DOCKERHUB_USERNAME }}
                    password: ${{ secrets.DOCKERHUB_TOKEN }}
    
                - name: Set up Docker
                  uses: docker/setup-buildx-action@v2
                  
                - name: Build and push flask-backend
                  uses: docker/build-push-action@v4
                  with:
                    context: ./flask-backend
                    file: ./flask/dockerfile
                    push: true
                    tags: ${{ secrets.DOCKERHUB_USERNAME }}/flask:${{ github.run_number }}/Flask:latest
                      
                - name: Build and push vue-frontend
                  uses: docker/build-push-action@v4
                  with:
                    context: ./vue-frontend
                    file: ./vue-frontend/dockerfile
                    push: true
                    tags: ${{ secrets.DOCKERHUB_USERNAME }}/vue_project:${{ github.run_number }}/vue_project:latest
        deploy: 
            name: server deploy
            runs-on: self-hosted
            needs: build-push
    
            steps:
              - name : Pull latest images
                run: |
                    docker pull ${{ secrets.DOCKERHUB_USERNAME }}/Flask:latest
                    docker pull ${{ secrets.DOCKERHUB_USERNAME }}/vue_project:latest
          
              - name: Stop and Remove Existing Containers and Networks
                run: |
                    docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)
                    docker network prune -f
    
              - name: Create Network and Run containers
                run : |
                  sudo docker compose up -d

              - name: Remove unused data
                run: |
                  docker system prune -af
  ```
## Testing
## Domain and SSL
we will use free domain provided freedns.afraid.org. Domain can be accessed through monjo.strangled.net 
due to ubuntu error. i cant manage to get ssl certificate from certbot/
