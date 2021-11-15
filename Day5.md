## Tasks Completed Today - 12/11/2021

[x] Complete FastAPI tutorial on Youtube. [Link](https://www.youtube.com/watch?v=GN6ICac3OXY)

[x] Join virtual class to learn about Docker and Docker Compose.

[x] Basic project for first week.
    
+ FastAPI
+ Docker, Docker Compose

Activities

With python installed, 

```
# check if you have python
$ which python

# check your current version of python
$ python --version
```
Create project folder

create virtual environment
```
python3 -m venv .proj
```
add virtual env path to gitignore

activate virtual environment
```
$ source path/to/virtualenv/bin/activate
```

check install packages
$ pip list

install the packages needed, thus, fastapi and uvicorn standard

```
$ pip install fastapi "uvicorn[standard]"
```

setup main.py for app

to run app,

```
$ uvicorn main:app --reload
```

with everything running...
create requirements.txt
```
$ pip freeze > requirements.txt
```

Setting up docker, docker compose

With Docker Installed
[Link](https://fastapi.tiangolo.com/deployment/docker/)
create Dockerfile
```Docker




```

Build docker
```
docker build -t <image> .

```
Run Image
docker run -p 8000:8000 -t -i <image>