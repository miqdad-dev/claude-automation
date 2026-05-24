# Networking Project: Simple Chat App

This is a simple chat application built using Python's built-in socket and threading libraries.

## What It Does

It allows multiple clients to connect to a server and send messages to each other.

## How It Works

- The server listens for incoming connections from clients.
- When a client connects, it sends a 'NICK' message to the server indicating it is ready to set its nickname.
- The server then sends a 'NICK' message to the client to prompt them to set their nickname.
- Once the nickname is set, the client can start sending messages to the server.
- The server broadcasts these messages to all connected clients.
- If a client disconnects, the server notifies all clients that the client has left the chat.

## How to Run

1. Run the server: `python server.py`.
2. In a new terminal window, run the client: `python client.py`.
3. Enter a nickname when prompted.
4. Start typing messages into the terminal. They will be broadcast to all connected clients.

## Example Usage