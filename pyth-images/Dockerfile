#FROM python:latest
#WORKDIR /app
#COPY . /app
#CMD ["python3","app.py"]
# Use a base Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY app.py /app

# Install dependencies (if you have any requirements.txt, you can use that)
RUN pip install flask

# Expose the port that Flask will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]