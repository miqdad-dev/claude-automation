# Key-Value DB

A simple in-memory key-value database with a command-line interface.

## How it works

The program uses a HashMap to store key-value pairs. It reads commands from standard input and writes responses to standard output. The supported commands are:

- `get <key>`: Prints the value for the given key. If the key does not exist, prints "Key not found".
- `set <key> <value>`: Sets the value for the given key, overriding any existing value.
- `delete <key>`: Removes the value for the given key.
- `exit`: Exits the program.

## How to run

1. Install Rust: https://www.rust-lang.org/tools/install
2. Clone this repository.
3. Run `cargo run` in the root directory of the repository.
4. Enter commands at the prompt.

## Example usage