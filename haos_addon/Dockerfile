FROM python:3.11-slim

RUN pip install --no-cache-dir flask openai

COPY . /app
WORKDIR /app

RUN chmod a+x /app/run.sh

CMD [ "/app/run.sh" ]
