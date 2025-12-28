# Distributed Systems Mini Project

This is a simple distributed system using Python and ZeroMQ. The system is composed of a server that will generate random numbers and send them to multiple clients.

## How it works

The project is composed of three parts:
- A server that generates random workloads and sends them to workers.
- Workers that receive tasks from the server, execute them and then send a confirmation to the sink.
- A sink that waits for confirmations from all workers.

## How to run

You will need to have Python and ZeroMQ installed on your machine.

To run the server, open a terminal and type: