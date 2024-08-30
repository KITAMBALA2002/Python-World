#!/usr/bin/env python3
import mysql.connector
from Security import connect_to_database

def new_book():

    print('Add any new book to the system')
    title=input('Add a book title here: ')
    author =input('Add the author here: ')
    publication =input('Add the publication date [yyyy-mm-dd]: ')
    genre =input('Add the book genre: ')
    isbn =input('Add the ISBN here: ')

    mydb = connect_to_database()
    if mydb is None:
        return

    cursor = mydb.cursor()
    cursor.execute('INSERT INTO Books (Title, Author,Publication,Genre,ISBN) VALUES (%s, %s,%s,%s,%s)', (title, author,
                    publication,genre,isbn))
    mydb.commit()
    print(f'{title} is added, please check!')

def remove_book():
    search_book=input('What book do you want remove: ').strip()

    mydb = connect_to_database()
    if mydb is None:
        return

    cursor = mydb.cursor()
    query = "SELECT * FROM Books WHERE Title = %s"
    cursor.execute(query, (search_book,))

    check =cursor.fetchone()
    if check:
        remove="DELETE FROM Books WHERE Title = %s"
        cursor.execute(remove,(search_book,))

        mydb.commit()
        print('The book is deleted!')

    else: print('Book can not be found')

def update_book():
    print('Update the book details here')
    search_book = input('What book do you want to update: ').strip()

    # Connect to the database
    mydb = connect_to_database()
    if mydb is None:
        return

    cursor = mydb.cursor()

    # Check if the book exists
    query = "SELECT * FROM Books WHERE Title = %s"
    cursor.execute(query, (search_book,))

    check = cursor.fetchone()
    if check:
        title = input("Add the new book title: ").strip()
        author = input("Add author: ").strip()
        publication = input("Add publication date [yyyy-mm-dd]: ").strip()
        genre = input("Add book genre: ").strip()

        update = """
            UPDATE Books
            SET Title = %s, Author = %s, Publication = %s, Genre = %s
            WHERE Title = %s
        """
        values = (title, author, publication, genre, search_book)
        cursor.execute(update, values)

        mydb.commit()

        print(f'The book titled "{search_book}" has been updated to "{title}".')

    else:
        print('Book cannot be found')

    cursor.close()
    mydb.close()

def manage_users():
    print('1. Add new user account.')
    print('2. Add delete the user account')
    try: 
        select=int(input('What is your option? '))
        if select == 1:
            username=input('Username: ')
            password= input('Password: ')
            email = input('Add email address: ')
            title =input ('Add the role [Admin,Librarian]: ')

            mydb = connect_to_database()
            if mydb is None:
                return
            cursor = mydb.cursor()

            if title == 'Admin':
                role='Admin'
                cursor.execute('INSERT INTO Admin (Username,Password,Email,Role) VALUES (%s, %s,%s,%s)', 
                               (username,password,email,role) )
                
                mydb.commit()
                print(f'{username} is addd to the Admin board.')
            elif title == "Librarian":
                role='Librarian'
                cursor.execute('INSERT INTO Librarian (Username,Password,Email,Role) VALUES (%s, %s,%s,%s)', 
                               (username,password,email,role) )
                
                mydb.commit()
                print(f'{username} is addd to the Librarian board.')

        elif select == 2:
            try:
                print('1. Remove Admin.')
                print ('2. Remove Librarian')

                choose=int(input('What is your choice? '))
                if choose == 1:
                        
                    browse_admin=input('Browse admin name: ').strip()

                    mydb = connect_to_database()
                    if mydb is None:
                        return

                    cursor = mydb.cursor()
                    query = "SELECT * FROM Admin WHERE Username = %s"
                    cursor.execute(query, (browse_admin,))

                    check =cursor.fetchone()
                    if check:
                        remove="DELETE FROM Admin WHERE Username = %s"
                        cursor.execute(remove,(browse_admin,))

                        mydb.commit()
                        print(f'{browse_admin} is removed successfully!')

                    else: print(f'{browse_admin} is not available, try new name!')
                elif choose == 2:
                    browse_librarian=input('Browse Librarian name: ').strip()

                    mydb = connect_to_database()
                    if mydb is None:
                        return

                    cursor = mydb.cursor()
                    query = "SELECT * FROM Librarian WHERE Username = %s"
                    cursor.execute(query, (browse_librarian,))

                    check =cursor.fetchone()
                    if check:
                        remove="DELETE FROM Librarian WHERE Username = %s"
                        cursor.execute(remove,(browse_librarian,))

                        mydb.commit()
                        print(f'{browse_librarian} is removed successfully!')

                    else: print(f'{browse_librarian} is not available, try new name!')
            except ValueError:
                print('Invalid value, please add a valid value!')

    except ValueError:
        print('Invalid value, please add a valid value!')
        
def view_report():
    print("\nVIEW REPORT\n")
    mydb = connect_to_database()
    if mydb is None:
        return

    cursor = mydb.cursor()
    cursor.execute("SELECT COUNT(*) AS Role FROM Admin")
    admin = cursor.fetchone()  
    if admin:
        total_admins = admin[0]
        print(f"Total Number of Admins: {total_admins}")

    cursor = mydb.cursor()
    cursor.execute("SELECT COUNT(*) AS Role FROM Librarian")
    library = cursor.fetchone()  
    if library:
        total_librarians = library[0]
        print(f"Total Number of Librarians: {total_librarians}")

    cursor = mydb.cursor()
    cursor.execute("SELECT COUNT(*) AS Role FROM Books WHERE Author = MOses P.M")
    library = cursor.fetchone()  
    if library:
        total_librarians = library[0]
        print(f"Total Number of Books by Author: {total_librarians}")

    cursor = mydb.cursor()
    cursor.execute("SELECT COUNT(*) AS Role FROM Books")
    library = cursor.fetchone()
    if library:
        total_librarians = library[0]
        print(f"Books by Genre: {total_librarians}")

    cursor = mydb.cursor()
    cursor.execute("SELECT COUNT(*) AS Publication FROM Books WHERE PublicationDate > '2000-01-01'")
    publish = cursor.fetchone()  
    if publish:
        total_years = publish[0]
        print(f"Books by Publication year: {total_years}")

    cursor = mydb.cursor()
    cursor.execute("SELECT COUNT(*) AS Role FROM Books WHERE ISBN")
    isbn = cursor.fetchone() 
    if isbn:
        total_isbn = library[0]
        print(f"Books by ISBN: {total_isbn}")