# Mini-hard Database Project

This project reads data from a CSV file and writes it to a SQLite database. It then reads the data from the SQLite database and prints it.

## How It Works

The project uses a Python script to interact with the SQLite database. It uses the pandas library to read the CSV file and to handle the data.

## How to Run

- Build the Docker image: `docker build -t databases .`
- Run the Docker image: `docker run -it --rm --name my-running-app databases`

## Example Usage

When the project is run, it will print the data from the SQLite database, which will look like this: