#!/usr/bin/env python3
import mysql.connector
from Security import connect_to_database

def return_book():
    username=input('Username: ')
    book_title= input("The Book Title: ")
    returned_date=input("Enter the return date [yyyy-mm-dd]: ")

    mydb = connect_to_database()
    if mydb is None:
        return

    cursor = mydb.cursor()
    query = "SELECT * FROM Borrowed WHERE Username = %s"
    cursor.execute(query, (username,))

    check =cursor.fetchone()
    if check:
        insert='INSERT INTO Returned_books (Username,Title,Return_date) VALUES (%s, %s,%s)'
        cursor.execute(insert,(username,book_title,returned_date))

        remove="DELETE FROM Borrowed WHERE Username = %s"
        cursor.execute(remove,(username,))
        print('The book has been added back!')

        mydb.commit()
    else: print('The book can not be found in the borrowed system!')

def check_return_book():
    search_book=input('\nWhat book are you searching: ').strip()
    username=input('Username: ').strip()

    mydb = connect_to_database()
    if mydb is None:
        return

    cursor = mydb.cursor()
    query = "SELECT * FROM Returned_books WHERE Title = %s AND Username = %s"
    cursor.execute(query, (search_book,username))

    check =cursor.fetchall()
    if check:
        print('The book is available')
    else: print('The book does not exist! checking borrowing data.')

def process_borrowing():
    username=input("Username: ")
    email=input("Email Address: ")
    role=input("Role: ")
    title=input("Title: ")
    isbn=input("Book ISBN: ")
    borrowed_date=input("Borrowed date: ")
    due_date=input("Due date: ")
    return_date=input("Return date: ")
    later_fine=int(input("Enter late return fine: "))

    mydb = connect_to_database()
    if mydb is None:
        return
    cursor = mydb.cursor()
    insert='INSERT INTO Borrowed (Username,Email,Role,Title,Book_ISBN,Borrowed_date,Due_date,Return_date,Fine) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(insert,(username,email,role,title,isbn,borrowed_date,due_date,return_date,later_fine))

    mydb.commit()
    print('Information is saved!')
