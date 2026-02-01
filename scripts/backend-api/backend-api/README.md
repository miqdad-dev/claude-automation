# User Registration API

This is a simple User Registration API built with Flask, Flask-RESTful, and SQLAlchemy.

## What it does
This API allows users to register by providing a unique username.

## How it works
It uses Flask-RESTful for creating the API resources and SQLAlchemy as the ORM. It uses an SQLite database to store the user data.

## How to run
1. Install the requirements:   
   `pip install -r requirements.txt`
2. Run the application:  
   `python app.py`

## Example usage
`POST /register` with JSON `{ "name": "username" }`.

## Architecture & Tradeoffs
The application uses the Flask web framework due to its simplicity and flexibility. SQLAlchemy is used as the ORM to handle database operations. The tradeoff is that this architecture may not be suitable for larger scale applications with more complex requirements.