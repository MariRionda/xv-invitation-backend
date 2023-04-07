# Define the base image
FROM python:3.7

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN python -m venv .venv
RUN .venv/bin/pip install -r requirements.txt

# Copy the start script
COPY start.sh .

# Set the start command
CMD ["/bin/bash", "start.sh"]
