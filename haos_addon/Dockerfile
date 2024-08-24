# Use a Home Assistant base image that is Alpine-based
ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:3.13
FROM $BUILD_FROM

# Install Python 3 and pip3 using Alpine's package manager
RUN apk add --no-cache python3 py3-pip

# Verify that pip3 is installed correctly
RUN pip3 --version

# Install Python 3, pip3, and build dependencies
RUN apk add --no-cache python3 py3-pip build-base python3-dev

# Install Flask using pip3
RUN pip3 install flask

# Copy your script to the appropriate directory
COPY run.sh /app/run.sh

# Ensure the script is executable
RUN chmod +x /app/run.sh

# Set the default command to run your script
CMD ["/app/run.sh"]