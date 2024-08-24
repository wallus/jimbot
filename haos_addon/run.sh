flask run
#!/usr/bin/env bash
set -e

# Load Bashio library
source /usr/lib/bashio/bashio.sh

# Set FLASK_APP environment variable
export FLASK_APP=app.py

export FLASK_RUN_HOST=0.0.0.0

# Retrieve configuration options
OPENAI_API_KEY=$(bashio::config 'OPENAI_API_KEY')
PORT=$(bashio::config 'port')

# Run the Flask app with the specified port
flask run --host=0.0.0.0 --port=${PORT}