# Imports
import sqlite3

# Visualize data print() statements
from icecream import ic as print

# 1 - Intialize Database
def get_connection(db_name):
    try:
        return sqlite3.connect(db_name)
    
    except Exception as e:
        print(f"Error: {e}")
        raise  

# 2 - Create a Table in Database
def create_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
    """

    try:
        with connection:
            connection.execute(query)
        print("Table was created!")

    except Exception as e:
        print(e)

# 3 - Add User to Database
def insert_user(connection, name: str, age: int, email: str):
    query = "INSERT INTO users(name, age, email) VALUES (?, ?, ?)"
    try:
        with connection:
            connection.execute(query, (name, age, email)) # do this to prevent sql injections
        print(f"User: {name} was added to your database!")

    except Exception as e:
        print(e)

# 4 - Query all Users in Database
def fetch_users(connection, condition: str = None) -> list[tuple]: 
    query = "SELECT * FROM USERS"

    if condition: # ex. condition = "age > 10", "name = 'Lookie'"
        query += f" WHERE {condition}"

    try:
        with connection:
            rows = connection.execute(query).fetchall()
        return rows
    
    except Exception as e:
        print(e)

# 5 - Delete a User from the Database
def delete_user(connection, user_id: str):
    query = "DELETE FROM users WHERE id = ?"

    try:
        with connection:
            connection.execute(query, (user_id,))
        print(f"USERID: {user_id} was deleted!")
    except Exception as e:
        print(e)

# 6 - Update User
def update_user(connection, user_id: int, email: str):
    query = "UPDATE users SET email = ? WHERE id = ?"

    try:
        with connection:
            connection.execute(query, (email, user_id))
        print(f"User ID {user_id} has a new email of {email}")

    except Exception as e:
        print(e)

# 7 - Add Multiply Users
def insert_users(connection, users: list[tuple[str, int, str]]):
    query = "INSERT INTO users (name, age, email) Values (?,?,?)"

    try:
        with connection:
            connection.executemany(query, users)
        print(f"{len(users)} users were added to the database")
    
    except Exception as e:
        print(e)

# Main Function Wrapper
def main():
    connection = get_connection('finance.db')

    try:
        # Create Table
        create_table(connection)

        start = input("Enter Option (Add, Delete, Update, Search, Add Many): ").lower()

        if start == 'add':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            insert_user(connection, name, age, email)
        
        elif start == 'search':
            print("All Users:")
            for user in fetch_users(connection):
                print(user)
        
        elif start == 'delete':
            user_id = int(input("Enter User ID: "))
            delete_user(connection, user_id)
        
        elif start == 'update':
            user_id = int(input("Enter User ID: "))
            new_email = input("Enter a new email: ")
            update_user(connection, user_id, new_email)
        
        elif start == "add many":
            users = [('QQ', 29, 'QQ@gmail.com'),
                     ('WW', 100, 'WW@gmail.com'),
                     ('MM', 63, 'MM@gmail.com')]
            insert_users(connection, users)

    finally:
        connection.close()

if __name__ == "__main__":
    main()