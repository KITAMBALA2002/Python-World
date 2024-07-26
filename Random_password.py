import re
import random


def generate_random_word(length):
    letters = 'a345bc678d79A0e0DfF456gHh9E0iDF34jk75l3RD45mYnTREoHJpVqrD123S42353Wstuvwxyz'
    word = ''
    for _ in range(length):
        word += random.choice(letters)
    return word

random_word = generate_random_word(8)
print(f"The generated password is : {random_word}")

