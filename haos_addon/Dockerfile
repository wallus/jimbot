# Use a Home Assistant base image
ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:3.13
FROM $BUILD_FROM

# Install Python 3, pip3, and virtualenv via apk
RUN apk add --no-cache python3 py3-pip py3-virtualenv

# Create and activate a virtual environment
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Install Flask inside the virtual environment
RUN pip3 install flask openai logging flask_cors

# Copy your script to the /app directory
COPY app.py /app/app.py
COPY templates /app/templates
COPY static /app/static

# Ensure the script is executable
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

WORKDIR /app

# Set the default command to run your script
CMD ["/app/run.sh"]
