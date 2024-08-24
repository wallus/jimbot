#!/usr/bin/env bash
set -e  # Exit immediately if a command exits with a non-zero status

# Debug statement to confirm script started
echo "Starting run.sh script..."

# Check if bashio is available
if command -v bashio >/dev/null 2>&1; then
    echo "bashio found"
    # Load Bashio library
    source /usr/lib/bashio/bashio.sh

    # Retrieve configuration options using bashio
    OPENAI_API_KEY=$(bashio::config 'OPENAI_API_KEY')
    PORT=$(bashio::config 'port')
else
    echo "bashio not found, using default values"
    # Provide fallback or default values
    OPENAI_API_KEY=${OPENAI_API_KEY:-"sk-dkv9oMuyXZ9YXJGaACj4TLIIB2gHuTS7Hu83Y-pRXzT3BlbkFJYhW7_XMFMyxeP05rO708BMF18z3beuWiK_5wgXrt8A"}
    PORT=${PORT:-8087}
fi

# Debug statement to check the values of OPENAI_API_KEY and PORT
echo "OPENAI_API_KEY: ${OPENAI_API_KEY}"
echo "PORT: ${PORT}"

# Set FLASK_APP environment variable
export FLASK_APP=haos_addon/app.py

# Debug statement to confirm FLASK_APP is set
echo "FLASK_APP is set to ${FLASK_APP}"

# Run the Flask app with the specified port
echo "Trying Flask app on port ${PORT}..."
flask run --host=0.0.0.0 --port=${PORT}

# Debug statement to confirm Flask app started
echo "Flask app started on port ${PORT}"

