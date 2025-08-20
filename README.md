# Librachat Backend
This repository is focused on organizing the back end of the Librachat application.
Working together with other Docker containers, it can run the entire application and
be modularized in a clear and concise way.


# Running the application

## Creating the venv and the app
To create the virtual environment inside of python, we need to have 
the python binary installed in our machine, and run the 
command:

```bash
python -m venv venv
```

With this, we can wait for some seconds, and the virtual environment
for development gonna be created and we can see in the files of our 
project folder.

## Installing the Django and DRF
To install the dango, and the REST framework for django, we need to run:

```bash
pip install django djangorestframework
```

## Running the docker
This component of the app uses docker to virtualize the needs of the project. So to run 
this part of the project, you gonna need to have docker installed inside of your machine.
After this, you can use the Docker desktop or the CLI of your OS, goes by your option.
To run the application, you gonna need to build it inside of your machine running the 
command:

```bash
docker build -t name_of_the_container
```

We suggest that the name of the container of beeing `librachat_backend`, like in the 
in the standard and original pattern of creating of the container.
After this, we can run the application in the container using the
command:

```bash
docker run -p 8000:8000 librachat_backend
```

and with this, you can go to the `localhost:8000` and see the application running without problems.