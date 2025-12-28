import zmq
import time

# Prepare our context and sockets
context = zmq.Context()

# Socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5558")

# Wait for start of batch
s = receiver.recv()

# Start our clock now
tstart = time.time()

# Process 100 confirmations
for task_nbr in range(100):
    s = receiver.recv()
    if task_nbr % 10 == 0:
        print(":", end="", flush=True)
    else:
        print(".", end="", flush=True)

# Calculate and report duration of batch
tend = time.time()
print("Total elapsed time: %d msec" % ((tend - tstart) * 1000))