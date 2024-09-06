# Pull official base image
FROM public.ecr.aws/y9p5b4c9/python:3.11.0-slim

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install -y poppler-utils
RUN apt-get install -y ffmpeg libsm6 libxext6 libgl1-mesa-glx
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Create static folder
RUN mkdir -p collect_static

# Copy project
COPY . .

EXPOSE 8000
