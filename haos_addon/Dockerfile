# Use a Home Assistant base image
ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:3.13
FROM $BUILD_FROM

RUN pip3 install flask

# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]