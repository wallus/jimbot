# Use a Home Assistant base image
ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:3.13
FROM $BUILD_FROM

# Install Python 3, pip3, and virtualenv via apk
RUN apk add --no-cache python3 py3-pip py3-virtualenv

# Create and activate a virtual environment
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Install Flask inside the virtual environment
RUN pip3 install flask openai logging

# Copy your script to the appropriate directory
COPY run.sh /
COPY app.py /
COPY templates /templates

# Ensure the script is executable
RUN chmod +x /run.sh

# Set the default command to run your script
CMD ["/run.sh"]