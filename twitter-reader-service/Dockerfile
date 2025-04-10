# Dockerfile for Twitter Reader Service
# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required packages
RUN pip3 install --no-cache -r requirements.txt

# Run the application
CMD ["python", "read-messages-from-x.py"]