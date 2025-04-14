# Dockerfile for API Service
# Use the official Python image from the Docker Hub - 3.12-slim is lightweight and suitable for production
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy and install libraries from requirements.txt first to leverage Docker cache
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app

# Run the application
CMD ["python", "api-service.py"]