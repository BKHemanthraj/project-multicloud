# Use the official Python image from DockerHub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory to the container
COPY . /app/

# Expose the port the app will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python3", "app.py"]
 
