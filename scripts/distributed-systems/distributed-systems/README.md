# Distributed Systems Mini Project

This project implements a simple distributed system using Python's multiprocessing library. It simulates a distributed system where each process represents a node that can send and receive messages from other nodes in the system.

## What it does

The nodes in our system can perform two main tasks concurrently:

1. Send a message to a random node in the system.
2. Receive a message from any node in the system.

## How it works

Each node is implemented as a separate Python process, with a message queue for communication. A node can send a message to any other node by adding the message to the recipient's message queue. Each node continuously checks its own message queue for new messages.

## How to run

Ensure that Python 3.6 or later is installed on your system. Then, from the root of the project, run: