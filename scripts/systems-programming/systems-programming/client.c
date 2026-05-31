#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define BUFFER_SIZE 1024
#define PORT 8080

int main() {
    struct sockaddr_in address;
    int sock = 0;
    char *message = "Hello from Client!";
    char buffer[BUFFER_SIZE] = {0};

    sock = socket(AF_INET, SOCK_STREAM, 0);

    address.sin_family = AF_INET;
    address.sin_port = htons(PORT);

    connect(sock, (struct sockaddr *)&address, sizeof(address));

    send(sock, message, strlen(message), 0);
    printf("Message sent\n");

    read(sock, buffer, BUFFER_SIZE);
    printf("Message received: %s\n", buffer);

    return 0;
}