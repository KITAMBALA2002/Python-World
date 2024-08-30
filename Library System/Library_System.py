#!/usr/bin/env python3
import Admin
import Librarian
import Student
import Security

print ('\nLIBRARY SYSTEM')

def admin_main():
    print('\nWelcome to Admin page!')
    print('You have access to the following;')
    print('\n1. Add Books')
    print('2. Remove Books')
    print('3. Updating Books')
    print('4. Manage User account')
    print('5. Viewing the report.')

    try:
        choose =int(input("Pick your option above: "))
        if choose ==1: Admin.new_book()
        elif choose ==2: Admin.remove_book()
        elif choose ==3: Admin.update_book ()
        elif choose ==4: Admin.manage_users()
    except ValueError:
        print('Insert th valid value!')

def librarian_main():
    print ('Welcome to Librarian page!')
    print('1. Process returning books.')
    print('2. Check return updates')
    print('3. Process borrowing books')
    try:
        choose=int(input("Enter the valid optioin: "))
        if choose ==1: Librarian.return_book()
        elif choose ==2: Librarian.check_return_book()
        elif choose ==3: Librarian.process_borrowing()
    except ValueError:
        print ('Invalid value! try again.')

def member_main():
    print ('Welcome to Member page!')
    print('1. Return the book')
    print('2. Search a book')
    print('3. Check borrowing data')
    try:
        choose=int(input("Enter the valid optioin: "))
        if choose ==1: Student.return_books()
        elif choose ==2: Student.search_book()
        elif choose ==3: Student.check_borrowing()
    except ValueError:
        print ('Invalid value! try again.')

while True:
        try:
            print ('1. Admin')
            print ('2. Librarian')
            print ('3. Member/Student')
            print ('4. Exit\n')
            try:
                choose=int(input('\nWhat is your option from the above? '))

                if choose == 1:
                    check=Security.admin_page()
                    if check:
                        admin_main()
                elif choose == 2:
                    check=Security.librarian()
                    if check:
                        librarian_main()
                elif choose == 3:
                    member_main()
                elif choose > 3 and choose <10:
                        print('\n')
                        break
                
            except ValueError:
                print ('Value error, please add valid value!')
        except ValueError:
            print('Add valid option!')
