#!/usr/bin/env python3
from Admin import new_book,remove_book,update_book,manage_users
from Librarian import return_book,check_return_book,process_borrowing
from Student import return_books,check_borrowing,search_book
print ('\nLIBRARY SYSTEM')

while True:
        try:
            print ('1. Admin')
            print ('2. Librarian')
            print ('3. Member/Student')
            print ('4. Exit\n')
            try:
                choose=int(input('\nWhat is your options from the above? '))

                if choose == 1:
                    print('\nWelcome to Admin page!')
                    print('You have access to the following;')
                    print('\n1. Add Books')
                    print('2. Remove Books')
                    print('3. Updating Books')
                    print('4. Manage User account')
                    print('5. Viewing the report.')

                    try:
                        choose =int(input("Pick your option above: "))
                        if choose ==1: new_book()
                        elif choose ==2: remove_book()
                        elif choose ==3: update_book ()
                        elif choose ==4: manage_users()
                    except ValueError:
                        print('Insert th valid value!')
                elif choose == 2:
                    print ('Welcome to Librarian page!')
                    print('1. Process returning books.')
                    print('2. Check return updates')
                    print('3. Process borrowing books')
                    try:
                        choose=int(input("Enter the valid optioin: "))
                        if choose ==1: return_book()
                        elif choose ==2: check_return_book()
                        elif choose ==3: process_borrowing()
                    except ValueError:
                        print ('Invalid value! try again.')

                elif choose == 3:
                    print ('Welcome to Member page!')
                    print('1. Return the book')
                    print('2. Search a book')
                    print('3. Check borrowing data')
                    try:
                        choose=int(input("Enter the valid optioin: "))
                        if choose ==1: return_books()
                        elif choose ==2: search_book()
                        elif choose ==3: check_borrowing()
                    except ValueError:
                        print ('Invalid value! try again.')
                elif choose > 3 and choose <10:
                        break
                
            except ValueError:
                print ('Value error, please add valid value!')
        except ValueError:
            print('Add valid option!')
