#!/usr/bin/env python3

import os
def pass_check(file):
    count_words=0

    if os.path.isfile(file):
        with open(file,'r') as f:
            read=f.read()
            count=read.split()

            for line in count:
                count_words +=1
            print('There are ',count_words,'words in '+file)
 

for line in os.listdir():
    pass_check(line)
        
