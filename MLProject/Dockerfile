FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y build-essential curl git

# Install MLflow
RUN pip install mlflow pandas scikit-learn

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Default entrypoint
ENTRYPOINT ["mlflow", "run", "."]
