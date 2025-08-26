# Force update v1
FROM python:3.9-slim

# ... the rest of your Dockerfile ...
# Set the working directory in the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's source code
COPY . .

# Expose the port Cloud Run will use (optional, but good practice)
EXPOSE 8080

# Run the Streamlit app using the $PORT environment variable
# Use the filename of your Streamlit script (e.g., dashboard.py)
CMD streamlit run streamlit_app.py --server.port=$PORT --server.headless=true