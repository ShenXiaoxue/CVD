# Snow research

First commit - July 2025



## Deployment Instruction
- Before running the project, make sure both the Docker and Docker Compose have been installed.

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04

- To run the DTOP system, first create a virtual environment in the main folder

For linux:
```bash
python3 -m venv env
```
- Then enter the environment

For linux:
```bash
source env/bin/activate
```
- Make sure you have Docker and Docker compose

- Run docker compose
```bash
sudo chmod 777 /var/run/docker.sock
docker compose build
docker compose up
```
## Access the website:

![Example Image](snowresearch.png)
