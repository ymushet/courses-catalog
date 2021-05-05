# Dockerfile
# Pull base image
FROM python:3.9
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /src
# Copy project
COPY . /src/
# Install dependencies
RUN pip install -r /src/requirements.txt