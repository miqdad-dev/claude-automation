import os
import sqlite3
import pandas as pd
import pytest

def test_database():
    # Connect to SQLite database
    conn = sqlite3.connect('example.db')

    # Read data from SQLite database
    df = pd.read_sql_query('SELECT * FROM sample', conn)

    # Check data
    assert df['name'][0] == 'John'
    assert df['age'][0] == 30

    assert df['name'][1] == 'Jane'
    assert df['age'][1] == 25

    assert df['name'][2] == 'Joe'
    assert df['age'][2] == 35

    # Close connection
    conn.close()