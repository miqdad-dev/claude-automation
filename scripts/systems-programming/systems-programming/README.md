# Systems Programming - File Copy Utility

This is a simple file copy utility implemented in C, demonstrating low-level file I/O operations.

## What it does

The utility copies a file from a source to a destination, using the POSIX `open`, `read`, `write`, and `close` system calls.

## How it works

The utility opens the source file for reading and the destination file for writing. It reads from the source file in chunks of 4096 bytes and writes each chunk to the destination file until the entire file is copied.

## How to run

1. Clone the repository and navigate into the `systems-programming` directory.
2. Compile the program with `make`.
3. Run the utility with `./main <source-file> <destination-file>`, replacing `<source-file>` and `<destination-file>` with the paths to the source and destination files, respectively.

## Example Usage