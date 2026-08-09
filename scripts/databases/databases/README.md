# MySQL Database Project

This project demonstrates how to set up a MySQL Database using Docker and Python. It creates a database, a table and inserts data into the table.

## How it works

The project uses Docker to host the MySQL Database and Adminer for database management. Python's mysql-connector-python library is used to connect with the database, execute SQL queries such as creating a database, creating a table, and inserting data into the table.

## How to run

1. Ensure that Docker is installed on your machine.
2. Navigate to the root directory of the project and run `docker-compose up -d`.
3. To run the Python script, make sure you have Python and the mysql-connector-python library installed. Run `python main.py`.

## Example Usage

Once the Docker containers are up and running, the database can be accessed via Adminer on `localhost:8080`. Use the following credentials to log in:

- System: MySQL
- Server: db
- Username: root
- Password: password
- Database: test_db

The Python script creates a database named 'test_db' and a table named 'users'. It then inserts data into the 'users' table.

## Notes on Architecture & Tradeoffs

This project is a simple demonstration of using Python with MySQL and Docker. For larger, production-ready applications, additional considerations such as error handling, connection pooling, transactions, and security would need to be taken into account.