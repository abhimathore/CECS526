
## Installation

Install the Python compiler if you dont have already.
Install Docker.


## Setting up Docker

1. After installing Docker run below code to check the images present in your local system.
```bash
docker images
```
2. Use this command to pull latest image of CentOs version 8 from DockerHub public repository.
```bash
docker pull centos:8
```
3. Use this command to create a container named MLOps of CentOs providing an interactive bash terminal.
```bash
docker create -it --name MLOps centos:8 /bin/bash
```
4. Use this command to run this container.
```bash
docker start MLOps
```
5. After starting, we will need to attach the interactive shell.
```bash
docker attach MLOps
```
6. Git clone the repository.
```bash
git clone <Repository_URL>
```
7. Before diving in we install all the requirements.
```bash
pip3 install -U -r requirements.txt
```

## Usage

1. Execute this command on command line to Train and Develop a model
```bash
python Model.py
```
This command will generate a .pkl file.

2. Execute this command to Run the driver code
```bash
python predict_salary.py
```

## Contributors

Abhishek Mathore,
Misha Chodavadiya,
Emily Xu

## License
[MIT](https://choosealicense.com/licenses/mit/)