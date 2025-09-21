import socket

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
print('Starting server...')
server_socket.bind(server_address)
server_socket.listen(1)

while True:
    # Wait for a connection
    print('Server listening on', server_address)
    client_socket, client_address = server_socket.accept()

    try:
        print('Connection from', client_address)

        # Receive the data
        data = client_socket.recv(1024)
        print('Received "%s"' % data)

        # Send data back
        print('Sending data back to the client')
        client_socket.sendall(b'Message received!')

    finally:
        # Clean up the connection
        client_socket.close()