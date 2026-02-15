# Simple Chat Server

This is a simple chat server built with Python's socket and threading libraries.

## What it Does

The server accepts connections from multiple clients and allows them to send messages to each other in real time.

## How it Works

The server creates a socket and binds it to an IP and port. It then listens for incoming connections. Each time a client connects, the server starts a new thread to handle that client's messages.

Clients connect to the server's IP and port and send messages to it. The server then broadcasts these messages to all connected clients.

## How to Run

To run the server, use the following command: