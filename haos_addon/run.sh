#!/usr/bin/env bash

set -e
source /usr/lib/bashio/bashio.sh
OPENAI_API_KEY=$(bashio::config 'OPENAI_API_KEY')

export FLASK_APP=app.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=8087
flask run
