# Use an official Python runtime as an image
FROM python:3.10

# The EXPOSE instruction indicates the ports on which a container 
# will listen for connections
# Since Flask apps listen to port 5000  by default, we expose it
EXPOSE 443

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction 
# creates a directory with this name if it doesn’t exist

# Install any needed packages specified in requirements.txt
COPY requirements.txt /
RUN pip install -r requirements.txt

# Run app.py when the container launches
COPY . /app
WORKDIR /app

# CMD ["gunicorn"  , "--bind", "0.0.0.0:443", "wsgi:app", "--config gunicorn_hooks_config.py"]
CMD ["gunicorn"  , "--config gunicorn_config.py"]
