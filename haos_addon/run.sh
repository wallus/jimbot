#!/usr/bin/with-contenv bashio
set -e

# Load Bashio library
source /usr/lib/bashio/bashio.sh

# Retrieve configuration options using bashio
OPENAI_API_KEY=$(bashio::config 'OPENAI_API_KEY')
PORT=$(bashio::config 'port')

# Set FLASK_APP environment variable
export FLASK_APP=app.py
export OPENAI_API_KEY=${OPENAI_API_KEY}

# Run the Flask app with the specified port
flask run --host=0.0.0.0 --port=${PORT}
