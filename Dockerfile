# Use the official Python image as the base image
FROM python:3.10.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application files into the container
COPY . .

# Expose the port that FastAPI is running on (default is 8000)
EXPOSE 8000

# Command to run the FastAPI application when the container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
