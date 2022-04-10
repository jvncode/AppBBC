# Base Image
FROM python:3.7

# Create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app

COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Default port
ARG ARG_DEFAULT_PORT=8000
EXPOSE $ARG_DEFAULT_PORT
ENV DEFAULT_PORT=${ARG_DEFAULT_PORT}

# Run server
ENTRYPOINT python manage.py runserver 0.0.0.0:${DEFAULT_PORT}
#CMD gunicorn appbbc.wsgi:application --bind 0.0.0.0:${DEFAULT_PORT}