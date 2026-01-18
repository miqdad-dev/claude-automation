# Simple RESTful API with Node.js and Express

This is a simple RESTful API built with Node.js and Express, which supports CRUD operations on a list of users stored in memory.

## How It Works

The API has five endpoints:

- GET /users: Returns a list of all users.
- POST /users: Adds a new user to the list.
- GET /users/:id: Returns the user with the given id, or 404 if no such user exists.
- PUT /users/:id: Updates the user with the given id, or 404 if no such user exists.
- DELETE /users/:id: Deletes the user with the given id, or 404 if no such user exists.

The users are stored in an in-memory array, so they will be lost if the server is restarted.

## How to Run

1. Install dependencies: `npm install`
2. Start the server: `npm start`
3. Run tests: `npm test`

## Example Usage

GET /users

Response: