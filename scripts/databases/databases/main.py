import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('example.db')

# Read CSV data
data = pd.read_csv('data/sample.csv')

# Write data to SQLite database
data.to_sql('sample', conn, if_exists='replace')

# Read data from SQLite database
df = pd.read_sql_query('SELECT * FROM sample', conn)

# Print data
print(df)

# Close connection
conn.close()