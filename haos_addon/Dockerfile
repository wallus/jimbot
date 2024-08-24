# Example for an Alpine-based image with bashio
ARG BUILD_FROM=ghcr.io/hassio-addons/base:9.2.0
# or for a Debian-based image
# ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base-debian:bullseye

FROM $BUILD_FROM

# Copy your run.sh script
COPY run.sh /app/run.sh

# Make sure the script is executable
RUN chmod +x /app/run.sh

# Set the default command to run your script
CMD ["/app/run.sh"]
