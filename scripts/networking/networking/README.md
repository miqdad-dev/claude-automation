# Simple Chat Server and Client
This project consists of a simple chat server and client using TCP sockets.

## What it does
The server waits for a connection from a client. Once connected, the client sends messages to the server which are then broadcasted to all other connected clients.

## How it works
Both the server and client use TCP sockets for communication. The server uses threading to handle multiple clients simultaneously.

## How to run
- Run the server: `python server.py`
- Run the client(s) in separate terminals: `python client.py`

## Example usage
- Start the server: `python server.py`
- Start a client and choose a nickname: `python client.py`
- Start another client and choose a different nickname: `python client.py`
- Send messages from one client, they will be received by all other clients.

## Notes on architecture & tradeoffs
This is a simple implementation and does not handle all possible edge cases. For example, if a client suddenly disconnects without notifying the server, it may cause the server to crash. A more robust implementation would include error handling for these situations.