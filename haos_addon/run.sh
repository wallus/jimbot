#!/usr/bin/with-contenv bashio
set -e

# Retrieve configuration options using Bashio, with defaults
OPENAI_API_KEY="$(bashio::config 'OPENAI_API_KEY')"
PORT="$(bashio::config 'port')"

# Set defaults if the values are not provided
PORT=${PORT:-8087}  # Default to port 8087
OPENAI_API_KEY=${OPENAI_API_KEY:-"OPENAI_API_KEY value is not set in the Addon configuration"}  # Default message for API key

# Debugging statements to check the values
echo "Using PORT: ${PORT}"
echo "Using OPENAI_API_KEY: ${OPENAI_API_KEY}"

# Set FLASK_APP environment variable
export FLASK_APP=app.py
export OPENAI_API_KEY=${OPENAI_API_KEY}

# Run the Flask app with the specified port
flask run --host=0.0.0.0 --port=${PORT}