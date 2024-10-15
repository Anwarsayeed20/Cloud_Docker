FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY scripts.py /app/

# Create the /home/data directory inside the container
RUN mkdir -p /home/data/output

# Copy text files to the container's /home/data directory
COPY IF.txt /home/data/
COPY AlwaysRememberUsThisWay.txt /home/data/

# Command to run the Python script
CMD ["python", "/app/scripts.py"]
