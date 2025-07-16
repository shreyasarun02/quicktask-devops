# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirement and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app
COPY app.py .

# Run the app
CMD ["python", "app.py"]