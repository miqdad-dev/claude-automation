#!/bin/bash

make

echo "Starting server..."
./server &

sleep 2

echo "Starting client..."
./client

pkill server