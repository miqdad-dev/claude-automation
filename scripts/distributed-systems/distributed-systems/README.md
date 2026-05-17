# Distributed Systems: RPC over RabbitMQ

This distributed system consists of a producer (client) that sends requests to a consumer (server) via RabbitMQ. The consumer computes the Fibonacci number at the requested index and returns the result to the client. 

## How it works

The client sends a request to the server with a unique correlation ID. The server computes the Fibonacci number at the requested index and sends the result back to the client, along with the correlation ID. The client waits for a response that matches its correlation ID.

## How to run

1. Install RabbitMQ and Python
2. Install the necessary Python modules using pip: