#!/usr/bin/env python3

import getpass
import mysql.connector

def connect_to_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="pablo_alimasi",
            password="2024Admin#",
            database="Library_System"
        )
        return mydb
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None
def admin_page():
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    mydb = connect_to_database()
    if mydb is None:
        return

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Admin WHERE Username = %s", (username,))
    user = cursor.fetchone()

    if user and user[2] == password: # Assuming user[2] is the password field
        return True
    else:
        print("Invalid username or password.")

    cursor.close()
    mydb.close()

def librarian():
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    mydb = connect_to_database()
    if mydb is None:
        return

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Librarian WHERE Username = %s", (username,))
    user = cursor.fetchone()

    if user and user[2] == password:
        return True
    else:
        print("Invalid username or password.")

    cursor.close()
    mydb.close()
