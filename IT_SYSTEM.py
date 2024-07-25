#!/usr/bin/env python3

import csv

students = {
    'Peace Maker': {'Age': 21, 'Nationality': 'Congo','Gender':'Male','Birthday':'14/08/2002'},
}
def student_registration():
    full_name=input('Enter your full name: ')
    age=int(input('Enter your age: '))
    nationality=input('What is your nationality? ')
    gender=input('Are you a Male or Female? ')
    birthday=input('Enter your date of birth [dd/mm/yyyy]: \n')

    students[full_name] = {'Age': age, 'Nationality': nationality,'Gender':gender,'Birthday':birthday}
    csv_file = 'students.csv'

    with open (csv_file,'r') as file1:
        read = csv.DictReader(file1)
        for line in read:
            if full_name in line['Name']:
                print('Student exist, please add a different student!')
                break
            else:

                with open(csv_file, mode='a', newline='') as file:
                    
                    writer = csv.writer(file)
                    #writer.writerow(['Name', 'Age', 'Nationality','Gender','BirthDay'])
                    for name, info in students.items():
                        writer.writerow([name, info['Age'], info['Nationality'],info['Gender'],info['Birthday']])
                        

                    print(f"\nStudent information has been saved to {csv_file}.\n")
                    break
        print('\n')

def update_information():
    old_name = input("\nEnter the name of the student to update: ")
    new_name = input("Enter the new name for the student: ")

    if old_name in students:
        students[new_name] = students.pop(old_name)
        print("\nUpdated Students information:")
        for name, info in students.items():
            print(f"Name: {name}, Age: {info['Age']}, Nationality: {info['Nationality']}, Gender: {info['Gender']}, Birthday: {info['Birthday']}")
        print('\n')

    else:
        print("Student not found!")
        
def search_info():
    name =input('Enter the full name: ')
    with open ('students.csv','r') as file:
        read=csv.DictReader(file)
        
        for line in read:
            if name in line['Name']:
                print (f'Name: {name}, Age:{line['Age']}, Nationality: {line['Nationality']}, Gender: {line['Gender']}')                
        print('\n')

            