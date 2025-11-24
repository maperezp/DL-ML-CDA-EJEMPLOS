# Use an official Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Other Dockerfile instructions...

# Create the model directory and copy the model file
RUN mkdir -p /app/model
COPY model/catboost_model.cbm /app/model

# Run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]