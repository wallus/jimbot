#!/bin/bash

# Directly use the environment variable for the OpenAI API key
export OPENAI_API_KEY=${OPENAI_API_KEY}

# Start the Node.js server
node /usr/src/app/server.js
