# Use a Home Assistant base image that is Alpine-based
ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:3.13
FROM $BUILD_FROM

# Install Python 3 and pip3
RUN apk add --no-cache python3 py3-pip

# Install virtualenv
RUN pip3 install virtualenv

# Create and activate a virtual environment
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Install Flask inside the virtual environment
RUN pip3 install flask

# Copy your script to the appropriate directory
COPY run.sh /app/run.sh

# Ensure the script is executable
RUN chmod +x /app/run.sh

# Set the default command to run your script
CMD ["/app/run.sh"]