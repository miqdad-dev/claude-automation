# Docker Nginx Static Website

This project demonstrates how to use Docker to host a static website using Nginx.

## How it works

The Dockerfile in this project is based on the nginx:alpine image. It copies the contents of the `website` directory into the appropriate directory for Nginx to serve them.

## How to run

1. Install Docker.
2. Clone this repository and navigate to its directory.
3. Build the Docker image: `docker build -t my-nginx .`
4. Run the Docker container: `docker run -d -p 8080:80 my-nginx`

The website is now available at `http://localhost:8080`.

## Example usage

After running the Docker container as described above, simply navigate to `http://localhost:8080` in your web browser. You should see a simple static website.

## Notes on architecture & tradeoffs

This project is very simple, so there aren't many tradeoffs to discuss. One potential improvement could be to use a Docker volume to host the website files, which would allow them to be updated without rebuilding the Docker image. However, this would complicate the setup slightly and was deemed unnecessary for this project.

The use of Docker allows this server to be run on any system that supports Docker, without needing to install and configure Nginx manually.