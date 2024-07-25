#!/usr/bin/env python3

from IT_SYSTEM import student_registration, search_info,update_information

print('\nWELCOME TO DATA MANAGEMENT SYSTEM\n')

while True:

    print('1. Add student information.')
    print('2. Update student information.')
    print('3. Search student by name.')
    print('4. Exit the program\n')

    option=int(input('Choose the option from above! '))

    if option == 1:
        student_registration()
    elif option ==2 :
        update_information()
    elif option == 3:
        search_info()
    elif option == 4:
        break
    else:
        print('Invalid operation!')

print('Thanks for using our system.')
