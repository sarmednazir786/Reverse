# Use a lightweight image for the base
FROM python:3.9-slim

# Create a working directory
WORKDIR /app

# Copy the Flask script and template (if applicable)
COPY . .

# Set the command to run the Flask app
CMD python3 cipher.py
