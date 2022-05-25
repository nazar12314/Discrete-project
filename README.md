# Discrete-project

### Content

- Autocomplete service(finished)
- Full-text engine(in progress)

### Generate your own Docker container from Dockerfile
***There are still some problem with Flask script, when containerized. To fix by tomorrow morning***

Dockerfile is an instruction for [Docker](https://www.docker.com/) to generate proper environment(image) for project.
This image can be containerized. Docker container is sort of virtual machine.

Let's run our environment step by step:
1. Install docker and dependecies. 
2. Open docker
3. Clone project repo
4. In your OS terminal enter project root directory and run following
    > docker build -t discrete .
    
    This will build your Docker image from Dockerfile specified, ignoring files and folders in .dockerignore.
    This step can take a little while. After created, run following to see your images
    > docker image ls -a
5. Let's run container. 
    > docker run -it -p 8080:3000 discrete /bin/bash
6. Change dir to backend and run driver.py
7. Change dir to frontend and run
    > npm start

Open localhost:8080