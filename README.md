# 

# Dockerise simple python script with no dependencies 
    cd  simple-python-app 
    docker build -t simple-python-app:v1 ./
    docker run -it simple-python-app:v1

# Dockerise simple python script with  dependencies 
    cd  python-docker-with-dependencies
    docker build -t python-dep:v1 ./
    docker run -it python-dep:v1


# Dockerise simple python script with dependencies in requirments.txt file

    cd  python-docker-requirments-txt
    docker build -t python-requirments:v1 ./
    docker run -it python-dep:v1



# Dockerise python Fast API app

We will futher use alpine image, to reduce the Docker image size
Standard python docker images size is around 1 GB, which makes it bulky/slow and contains a lot of components we will never use in most of the cases.
Best practice is to try to start with a minimum size image and add only components we need

    cd fast-api
    docker build -t fast-api:v1 ./
    docker run -p 80:80 fast-api:v1

# Dockerise python Flask Docker app

    cd flask-docker
    docker build -t flask-alpine:v1 ./
    docker run -p 8080:8080  flask-alpine:v1



# How to start a new Django Project
### Install django-admin 
    pip3 install django
    django-admin --version
    django-admin startproject django_project .
    python3 manage.py runserver

Notes: 

- update your port in manage.py (default is using 8000)

    from django.core.management.commands.runserver import Command as runserver
    runserver.default_port = "8080"
    
- add Allowed hosts in settings.py file  in django_project folder
    ALLOWED_HOSTS = ['0.0.0.0']

# Dockerise python Django Docker app

    cd django-docker
    docker build -t django-docker:v1 ./
    docker run -p 8080:8080 django-docker:v1
 