# Database Creation Project

This project creates and populates a SQLite database with user information using Flask and SQLAlchemy.

## How It Works

The project uses a Flask application to handle HTTP requests. When a POST request is made to the '/user' endpoint with a JSON payload containing 'name' and 'email' fields, a new user is created in the database.

## How to Run

1. Build the Docker image: `docker build -t my-python-app .`
2. Run the Docker image: `docker run -p 4000:80 my-python-app`

You can then make a POST request to 'localhost:4000/user' with a JSON payload to create a new user.

Example: