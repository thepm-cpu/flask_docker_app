# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source
COPY . .

# Expose the port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
