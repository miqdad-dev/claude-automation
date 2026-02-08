# Docker Compose App

This application uses Docker Compose to manage a multi-container application that includes a Node.js/Express.js app, a Postgres database, and a Redis cache.

## How It Works

The application uses Docker Compose to define and run the multi-container application. The `docker-compose.yml` file defines the services that make up the application, which include the Node.js app, the Postgres database, and the Redis cache. The services are isolated in their own containers, but can interact with each other as defined in the `docker-compose.yml` file.

The Node.js app uses the `pg` and `redis` modules to interact with the Postgres database and Redis cache, respectively.

## How to Run

1. Install Docker and Docker Compose.
2. Clone this repository and navigate to the `devops-infrastructure` directory.
3. Run `docker-compose up` to start the services.
4. Visit `http://localhost:5000` in your browser.

## Example Usage

When you visit `http://localhost:5000`, the application queries the current timestamp from the Postgres database, stores it in the Redis cache, then retrieves it from the cache and displays it.

## Architecture & Tradeoffs

This application uses a simple architecture with three services, each running in its own container. This allows each service to be developed and deployed independently, but also allows them to interact as needed.

However, there are tradeoffs associated with this architecture. Docker can introduce additional complexity, especially for developers unfamiliar with containerization. Additionally, while Docker Compose makes it easy to define and run multi-container applications, it may not be suitable for production environments, which may require a more robust orchestration tool like Kubernetes.