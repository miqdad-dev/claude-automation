import socket

# Set up the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
print('Connecting to %s port %s' % server_address)
client_socket.connect(server_address)

try:
    # Send data
    message = 'Hello, Server!'
    print('Client sending message:', message)
    client_socket.sendall(message.encode('utf-8'))

    # Look for the response
    data = client_socket.recv(1024)
    print('Server responded with:', data.decode('utf-8'))

finally:
    print('Closing socket')
    client_socket.close()