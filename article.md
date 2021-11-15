# FASTAPI and Docker

[Link 1](https://realpython.com/fastapi-python-web-apis/)
[Link 2](https://svitla.com/blog/flask-vs-fastapi-for-building-api)

Disclaimer: All commands may work in Linux or Mac OS

Latest Stackover research shows that about 59 top companies use FastAPI, wow, [See list here](https://stackshare.io/fastapi),. In about 3 years (since 2018), FastAPI has proven to be a big 'F' (Force) to battle with.

In this brief introduction to building APIs with FastAPI, we look at what makes FAstAPI different and go through step-by-step process of getting your API up and running. For a bonus, we use Docker to create an image of your project - build here, run anywhere.

Application Programming Interface(API) can be seen as a waiter/waitress at a bar. It takes orders(requests) from you(Web client/browser), sends to the chef(server), chef provides your order (response-mostly JSON) to waiter and waiter serves you with response. With that said, APIs are really useful because they allow your application to access data and communicate with other software or microservices. A typical use of API is when your Android App is able to get weather update of your current location within a matter of seconds. How does it do that...

With the concept of API cleared, let's get to business.

What is FASTAPI
Well it is surely fast as the name suggests. FastAPI is a Python web framework for building APIs. But the reason why it has gained popularity is its performance as compared it counterparts.

If you want to build and deploy API within seconds the you surely have have to consider using FastAPI because:
 + It is Fast
 + Helps reduce bugs
 + Easy to use
 + Robust and 
 + Intuitive

Why use FASTAPI
If not for anything, then personally I will choose Fast API because time is money. But to me what makes FastAPI stand out is that it has documentation feature out of the box. with just 
```
your-domain.name/docs
or
your-domain.name/redoc
```
you get the whole documentation for your just completed API, no sweat right.

Prerequisites
You are motivated to try out this modern Python framework, wait, are you a Pythonista.. If not then you are just like me. Anyways that shouldn't be a bother. Go through this simple introduction to Python basics [Link](https://blog.teclado.com/30-days-of-python).

+ Any operating system will do but this article focuses on Linux and Mac users
+ Python3.6 and above
+ Latest Verion of Docker installed


Creating your first
In this introduction, we build a simple API that returns "Hello" and any name you add.

Create a new folder for your project, mine will be sayhello

Navigate to the folder. In your terminal run command to install virtualenv python module
pip3 install virtualenv

Whiles in the project directory, create a new virtual environment by running 
python3 -m venv .sayhelloenv

To activate your new python virtual environment, run:

source .sayhelloenv/bin/activate

Install all fastapiand uvicorn using ;
pip3 install fastapi "uvicorn[standard]"

with all set, create a new file main.py and add the code snippet

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_root(name: str):
    return {"greeting": f"Hello! {name}, you're welcome"}
```

Run you app using command to start your server
```
uvicorn main:app --reload
```

Now you have a working api, to check if it works, open a new tab in you browser and enter
http://localhost:8000/?name=Yourname

you can stop your local server by hitting
```
CTRL + C
```
Now you app is ready for deployment - Now Docker comes in

Create a requirements.txt to contain all dependencies of you project like so:

```
pip3 freeze > requirements.txt
```

Create a file and name it Dockerfile in the same folder as main.py
``` docker
FROM python:3.9
COPY . .
COPY ./requirements.txt ./requirements.txt
WORKDIR /.

EXPOSE 8000:8000
RUN pip3 install -r requirements.txt
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
```
with the file saved, build the docker image using the command
```
docker build -t sayhelloapp .
```
Patience moves mountains, you will be done in no time.

Run docker image using the command
```
docker run -p 8000:8000 -t -i sayhelloapp
``
run localhost:8000/?name=Yourname
YAAAS, you have done it.

You can find the link to project [here](#)

But this is just the beginning. Keep learning and build cool stuff with FastAPI.
