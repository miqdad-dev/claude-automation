# Simple Chat Server and Client

This project provides a simple implementation of a server-client chat system using Python's `socket` library.

## How it works

The server listens for incoming connections. When a client connects, the server sends a 'NICK' message to request the client's nickname. The nickname is used to identify the user in the chat.

The client sends and receives messages in separate threads: one thread listens for incoming messages and prints them, and the other thread waits for user input and sends those messages.

If a client disconnects, the server broadcasts a message to the others to inform them.

## How to run

1. Run the server: `python server.py`.
2. In a separate terminal, run the client: `python client.py`.

## Example usage

After starting the server and client, you will be prompted to enter a nickname. After entering a nickname, you can start typing messages.

## Architecture & Tradeoffs

This is a basic implementation, so it doesn't support features like direct messages or user authentication. The server broadcasts all messages to all clients, so there's no privacy. Also, the server doesn't keep any history, so if a client disconnects they lose all previous messages.

The server and client are both single-threaded, so they can't process multiple requests simultaneously. However, this makes the code simpler and easier to understand.