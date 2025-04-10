# Dockerfile for API Service
# Use the official Python image from the Docker Hub - 3.12-slim is lightweight and suitable for production
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required packages - dependency management
RUN pip3 install --no-cache -r requirements.txt

# Run the application
CMD ["python", "api-service.py"]