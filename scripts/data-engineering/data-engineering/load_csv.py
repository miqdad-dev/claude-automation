import csv
import psycopg2
from psycopg2 import sql

def load_csv_to_db(file_name, table_name):
    conn = psycopg2.connect(
        host="localhost",
        database="testdb",
        user="postgres",
        password="password"
    )
    cur = conn.cursor()

    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        columns = next(reader) 
        query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
            sql.Identifier(table_name),
            sql.SQL(', ').join(map(sql.Identifier, columns)),
            sql.SQL(', ').join(sql.Placeholder() for _ in columns)
        )
        for row in reader:
            cur.execute(query, row)

    conn.commit()
    cur.close()
    conn.close()