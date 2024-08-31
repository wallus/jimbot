#!/usr/bin/with-contenv bashio
set -e

echo "---> Starting at: $(date '+%Y-%m-%d %H:%M:%S')"

# Retrieve configuration options using Bashio, with defaults
OPENAI_API_KEY="$(bashio::config 'openai_api_key')"
PORT="$(bashio::config 'port')"

# Set defaults if the values are not provided
PORT=${PORT:-5767}  # Default to port 8087
OPENAI_API_KEY=${OPENAI_API_KEY:-"OPENAI_API_KEY value is not set in the Addon configuration"}  # Default message for API key

# Set FLASK_APP environment variable
export FLASK_APP="app.py"
export OPENAI_API_KEY=${OPENAI_API_KEY}

# Run the Flask app with the specified port
flask --app app run --host=0.0.0.0 --port=${PORT}