from mysql_connector import create_connection, create_database, create_table, execute_query

create_database_query = "CREATE DATABASE test_db"
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT, 
  name TEXT NOT NULL, 
  email TEXT NOT NULL UNIQUE, 
  age INT, 
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""

insert_users = """
INSERT INTO users (name, email, age) VALUES 
('James', 'james@example.com', 25),
('Julia', 'julia@example.com', 30),
('Richard', 'richard@example.com', 35),
('Diana', 'diana@example.com', 40)
"""

connection = create_connection("db", "root", "password")
create_database(connection, create_database_query)
create_table(connection, create_users_table)
execute_query(connection, insert_users)