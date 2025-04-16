FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . . 
EXPOSE 5000
CMD ["python3", "youface.py"]

# Use Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy everything into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Run the Python app
CMD ["python", "youface.py"]

