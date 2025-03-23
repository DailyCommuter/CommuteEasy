import sqlite3

# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect("appname.db")
cursor = connection.cursor()

# Execute SQL commands
cursor.execute("DROP TABLE IF EXISTS user;")
cursor.execute("DROP TABLE IF EXISTS post;")

cursor.execute("""
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);
""")

# Commit changes and close the connection
connection.commit()
connection.close()

# Maybe we'll need later? I would assume not
# CREATE TABLE post (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   author_id INTEGER NOT NULL,
#   created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   title TEXT NOT NULL,
#   body TEXT NOT NULL,
#   FOREIGN KEY (author_id) REFERENCES user (id)
# );