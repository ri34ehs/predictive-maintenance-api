# api/Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Install Gunicorn, a production-ready web server
RUN pip install gunicorn

# Copy and install dependencies from requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application files
# This includes app.py and the 'models' folder
COPY . .

# Run the web server with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]