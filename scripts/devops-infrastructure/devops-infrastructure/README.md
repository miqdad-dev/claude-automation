# DevOps Infrastructure Project

## What it does
This project sets up a small environment using Docker, Docker Compose, and Python. It creates a Flask web application and a Redis instance, then links them together.

## How it works
* The web application uses Flask as the web framework and Redis as the database.
* Docker Compose is used to define and run the multi-container application.
* The application counts the number of visits to the homepage and stores the count in Redis.

## How to run
1. Install Docker and Docker Compose.
2. Clone the repository.
3. Navigate to the project directory.
4. Run `docker-compose up`.

## Example usage
After running `docker-compose up`, visit `localhost:5000` in your web browser. The webpage will display a greeting, the hostname, and the visit count. The visit count will increase with each page reload.

## Architecture & Trade-offs
* Docker and Docker Compose are used for easy setup and teardown of the environment.
* Flask is a lightweight web framework, so it is suitable for this small project.
* Redis is used for its simplicity and performance but does not provide the functionality of a full-fledged database.