#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define BUFFER_SIZE 1024
#define PORT 8080

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int address_length = sizeof(address);
    char buffer[BUFFER_SIZE] = {0};
    
    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);
    
    bind(server_fd, (struct sockaddr *)&address, sizeof(address));
    
    listen(server_fd, 3);
    
    new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&address_length);
    
    read(new_socket, buffer, BUFFER_SIZE);
    printf("%s\n", buffer);
    
    send(new_socket, buffer, strlen(buffer), 0);

    return 0;
}