# 1. Start with an official Python base image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the project files into the container
COPY . .

# 5. Expose the port the app runs on
EXPOSE 5000

# 6. Define the command to run the application
CMD ["python", "api/app.py"]