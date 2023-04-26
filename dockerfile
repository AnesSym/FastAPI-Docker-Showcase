# Use the official Python image as the base image
FROM python:3.9-alpine

# Set the working directory
WORKDIR /fastapi-app

# Copy the application code
COPY . /fastapi-app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Set the default command
CMD ["python", "main.py"]

