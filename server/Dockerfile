# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8.3-alpine


# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

#PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B)
ENV PYTHONDONTWRITEBYTECODE 1

# RUN apk update && apk add build-base python3-dev py-pip jpeg-dev zlib-dev openssl-dev gcc libffi-dev postgresql-dev



ENV LIBRARY_PATH=/lib:/usr/lib

# create root directory for our project in the container
RUN mkdir /taxiapp

# Set the working directory to /pyjs
WORKDIR /taxiapp

# Copy the current directory contents into the container at /pyjs
ADD . /taxiapp/

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r /requirements.txt
RUN apk del .tmp

# upgrade pip
RUN pip install 

#install the requirements
RUN pip install -r requirements.txt


# The above commands tell Docker to:

#     - Install system-level dependencies
#     - Make a new “/taxiapp” directory in the container
#     - Set that directory as the working directory (similar to using cd to step inside it)
#     - Copy over the rest of the files and folders
#     - Run pip install to install the latest version of pip along with any Python dependencies
