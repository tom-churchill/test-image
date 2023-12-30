# Use a Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy Python script to the container
COPY cpu_load.py /app

# Install required Python packages
RUN pip install flask

# Expose port 8080 for HTTP server
EXPOSE 80

# Run the Python script when the container starts
CMD ["python", "cpu_load.py"]
