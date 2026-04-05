import pytest
import threading
import time
from server import Server
from client import Client

def test_chat():
    server = Server(host='127.0.0.1', port=55556)
    client1 = Client(nickname='Alice', host='127.0.0.1', port=55556)
    client2 = Client(nickname='Bob', host='127.0.0.1', port=55556)

    server_thread = threading.Thread(target=server.run)
    server_thread.start()
    time.sleep(1)  # Give server time to start

    client1_thread = threading.Thread(target=client1.run)
    client1_thread.start()

    client2_thread = threading.Thread(target=client2.run)
    client2_thread.start()

    time.sleep(1)  # Give clients time to connect

    assert len(server.clients) == 2
    assert len(server.nicknames) == 2
    assert server.nicknames == ['Alice', 'Bob']

    # Send a message from client1
    client1.client.send('Hello, Bob!'.encode('ascii'))
    time.sleep(1)  # Give message time to be received

    # Check that client2 received the message
    assert 'Hello, Bob!' in client2.client.recv(1024).decode('ascii')