# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies needed for GeoPandas and Speedtest
RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set the PYTHONPATH so it can find the 'src' folder
ENV PYTHONPATH="/app/src"

# Expose the port FastAPI will run on
EXPOSE 8080

# Command to run the application
# Cloud Run expects the app to listen on $PORT
CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-8080}"]
