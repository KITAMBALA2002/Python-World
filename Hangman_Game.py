#!/usr/bin/env python3
#A text based game where the user has to guess a word letter by letter
import random
print('WELCOME')
print('This is a Hangman Game. You will guess a word by the given word length.\n')

names=['Isaya','AMISI','SHUKURU','PABLOS','ALIMASI','BYONCE','BYAKO','ALBERT','SHAKES','AMANI','PORTUGAL','ISAICAH']
name_list=random.choices(names)

alpha=0
count=0
for line in name_list:
    #search=input('Guess a word: ')
    print('The length of the word is',len(line))

    while count <len(line):
        alpha +=1
        count +=1
        alphabet=input(f'Enter alphabet {alpha}: ')
        with open ('Alphabets.txt','a') as file:
            write=file.write(alphabet)
            

    with open('Alphabets.txt','r') as file:
        read=file.read()
        if line == read:
            print('\nCongratulations.....You got the word.')
            with open('Alphabets.txt','w') as file:
                write_file=file.write('')
        else:
            print('\nYour search is',read)
            print('You fail, the answer is',line)
            with open('Alphabets.txt','w') as file:
                write_file=file.write('')

