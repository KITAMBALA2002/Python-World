#!/usr/bin/env python3
from Security import connect_to_database

def return_books():
    username=input('Username: ')
    book_title= input("The Book Title: ")
    returned_date=input("Enter the return date [yyyy-mm-dd]: ")

    mydb = connect_to_database()
    if mydb is None:
        return

    cursor = mydb.cursor()
    query = "SELECT * FROM Borrowed WHERE Username = %s AND Title = %s"
    cursor.execute(query, (username,book_title))

    check =cursor.fetchone()
    if check:
        insert='INSERT INTO Returned_books (Username,Title,Return_date) VALUES (%s, %s,%s)'
        cursor.execute(insert,(username,book_title,returned_date))

        remove = "DELETE FROM Borrowed WHERE Title = %s AND Username = %s"
        cursor.execute(remove, (book_title, username))

        print('The book has been added back!')

        mydb.commit()
    else: print('The book can not be found in the borrowed system!')
def search_book():    
    search_book =input ('Enter the book title: ')
    mydb = connect_to_database()
    if mydb is None:
        return

    cursor = mydb.cursor()
    query = "SELECT * FROM Books WHERE Title = %s"
    cursor.execute(query, (search_book,))

    check =cursor.fetchall()

    data=['Book Title','Author','Published','Genre','Book ISBN']
    if check:
        print('\n')
        for line in check:
            for i, line2 in enumerate(line):
                print(f"{data[i]}: {line2}")
    else: print('Book can not be found')

def check_borrowing():
    username =input ('Enter username: ')
    mydb = connect_to_database()
    if mydb is None:
        return

    cursor = mydb.cursor()
    query = "SELECT Username,Title,Book_ISBN,Borrowed_date,Due_date,Return_date,Fine FROM Borrowed WHERE Username = %s"
    cursor.execute(query, (username,))

    check =cursor.fetchall()

    data=['Username','Book Title','Book ISBN','Borrowed_date','Due_date','Return_date','Fine']
    if check:
        print('\n')
        for line in check:
            for i, line2 in enumerate(line):
                print(f"{data[i]}: {line2}")
            print('\n')
    else: print('Username does not exist!')
