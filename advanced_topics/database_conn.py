import sqlite3
import streamlit as st

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, age INTEGER)''')
conn.commit()

# Function to add a new user
def add_user(username, age):
    c.execute("INSERT INTO users VALUES (?,?)", (username, age))
    conn.commit()

# Function to fetch all users
def get_all_users():
    c.execute("SELECT * FROM users")
    return c.fetchall()

# User input
username = st.text_input("Username")
age = st.number_input("Age", min_value=1, max_value=100, step=1)
if st.button('Add User'):
    add_user(username, age)

# Display users
st.write("Users:")
users = get_all_users()
for user in users:
    st.write(user)

# Close the connection to the database
conn.close()
