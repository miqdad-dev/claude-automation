import multiprocessing
import random
import time


class Node(multiprocessing.Process):
    def __init__(self, id, queues):
        super().__init__()
        self.id = id
        self.queue = queues[id]
        self.queues = queues

    def run(self):
        while True:
            # Send a message to a random node.
            recipient_id = random.choice(list(self.queues.keys()))
            if recipient_id != self.id:
                message = f"Hello, Node {recipient_id}!"
                self.queues[recipient_id].put((self.id, message))

            # Check for new messages.
            while not self.queue.empty():
                sender_id, message = self.queue.get()
                print(f"Node {self.id} received message from Node {sender_id}: {message}")

            time.sleep(1)


def main():
    num_nodes = 5
    queues = {i: multiprocessing.Queue() for i in range(num_nodes)}
    nodes = [Node(i, queues) for i in range(num_nodes)]

    for node in nodes:
        node.start()

    for node in nodes:
        node.join()


if __name__ == "__main__":
    main()