# Simple CRUD API with Node.js, Express, and MongoDB

This is a simple backend API application that provides CRUD operations on a MongoDB database. It uses Node.js and Express.

## What it does

This application provides a simple REST API to interact with a MongoDB database collection. The collection contains documents with two fields: `title` and `description`.

## How it works

The application is a simple Express server that connects to a MongoDB database. It provides four endpoints:

1. `GET /items` to list all items.
2. `POST /items` to create a new item.
3. `PUT /items/:id` to update an existing item.
4. `DELETE /items/:id` to delete an item.

## How to run

1. Clone the repository.
2. Install dependencies with `npm install`.
3. Run the server with `npm start`.
4. Run tests with `npm test`.

## Example usage

To list all items: `curl localhost:3000/items`

## Notes on architecture & tradeoffs

This is a simple application designed to demonstrate a CRUD API with Node.js and MongoDB. It does not include any authentication or authorization mechanisms. If you wanted to use this in a production environment, you would need to add those features.