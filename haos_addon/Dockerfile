ARG BUILD_FROM
FROM $BUILD_FROM

RUN pip3 install flask

# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]