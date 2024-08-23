FROM node:16

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install --verbose

COPY . .

# Copy the run.sh script to the root of the container
COPY run.sh /run.sh

# Copy the public directory (if you have one) and other necessary files
COPY public /usr/src/app/public
COPY server.js /usr/src/app/server.js

# List files in the root to verify run.sh is there
RUN ls -l /

# If the script is found, make it executable
RUN chmod +x /run.sh

# Ensure that /bin/bash is used to run the script
CMD ["/bin/bash", "/run.sh"]

