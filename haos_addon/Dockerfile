# Use a Debian/Ubuntu-based Home Assistant base image
ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:debian
FROM $BUILD_FROM

# Install Python 3 and pip3
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Flask
RUN pip3 install flask

# Copy your script
COPY run.sh /app/run.sh

# Make sure the script is executable
RUN chmod +x /app/run.sh

# Set the default command to run your script
CMD ["/app/run.sh"]