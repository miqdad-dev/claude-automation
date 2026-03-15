#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char **argv) {
    if (argc != 3) {
        printf("Usage: %s <source-file> <destination-file>\n", argv[0]);
        return 1;
    }

    int src_fd = open(argv[1], O_RDONLY);
    if (src_fd == -1) {
        perror("open source file");
        return 1;
    }

    int dest_fd = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (dest_fd == -1) {
        perror("open destination file");
        return 1;
    }

    char buf[4096];
    ssize_t bytes;
    while ((bytes = read(src_fd, buf, sizeof buf)) > 0) {
        if (write(dest_fd, buf, bytes) != bytes) {
            perror("write");
            return 1;
        }
    }

    if (bytes == -1) {
        perror("read");
        return 1;
    }

    close(src_fd);
    close(dest_fd);

    return 0;
}