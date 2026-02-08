# Use official Node.js runtime as base image
FROM node:14

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the workspace directory
COPY package*.json ./

# Install all dependencies
RUN npm install

# Bundle app source  
COPY . .

# Make port 5000 available to the outside world
EXPOSE 5000

# Start the application
CMD [ "node", "app.js" ]