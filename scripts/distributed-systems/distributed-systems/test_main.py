import multiprocessing
import main


def test_node():
    queues = {0: multiprocessing.Queue(), 1: multiprocessing.Queue()}
    node = main.Node(0, queues)
    node.start()

    # Wait for the node to send a message.
    time.sleep(2)

    assert not queues[1].empty()

    sender_id, message = queues[1].get()
    assert sender_id == 0
    assert message == "Hello, Node 1!"

    node.terminate()
    node.join()