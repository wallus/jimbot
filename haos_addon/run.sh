#!/usr/bin/env bash
set -e

source /usr/lib/bashio/bashio.sh

# Retrieve configuration options
OPENAI_API_KEY=$(bashio::config 'OPENAI_API_KEY')
PORT=$(bashio::config 'port')

export OPENAI_API_KEY=$OPENAI_API_KEY
export FLASK_APP=app.py

flask run --host=0.0.0.0 --port=${PORT}