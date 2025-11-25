# Base image: Use the same python version as our environment
FROM python:3.10.6-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency list
COPY requirements.txt .

# Install dependencies
# (We add --no-cache-dir to keep the image small)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Install our local package
RUN pip install -e .

# Expose the ports for API (8000) and Frontend (8501)
EXPOSE 8000
EXPOSE 8501

# Make the startup script executable
RUN chmod +x run_app.sh

# The command to run when the container starts
CMD ["./run_app.sh"]
