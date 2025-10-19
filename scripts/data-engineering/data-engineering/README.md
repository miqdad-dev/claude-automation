# CSV Loader

This is a simple CSV file loader that loads data from CSV file into a PostgreSQL database.

## How it works

The script `load_csv.py` reads a CSV file row by row and inserts each row as a new record in the specified PostgreSQL table.

## How to run

1. Ensure you have Python and PostgreSQL installed on your machine.
2. Install the required Python library: `pip install psycopg2`.
3. Update the database connection configuration in `load_csv.py` if needed.
4. Run the script with the CSV file name and the database table name as arguments: `python load_csv.py <file_name> <table_name>`.

## Example usage