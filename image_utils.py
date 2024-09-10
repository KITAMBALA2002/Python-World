#!/usr/bin/env python3
import os
from PIL import Image

print('IMAGE MANIPULATION SCRIPT')

def rename_image(image,new_photo):

    if os.path.exists(image):
        im = Image.open(image)
        new_name=im.resize((840,680))
        new_name.save(new_photo)
        os.remove(image)
        print(f"{image} deleted.")
    else:
        print(f"{image} does not exist.")
        
def change_resize(image,width,height):
    if os.path.exists(image):
        im = Image.open(image)
        new_name=im.resize((width,height))
        new_name.save('Nacho.jpg')
        print(f"{image} loading.")
        new_name.show()
    else:
        print(f"{image} does not exist.")

def rotate_image(image,number):
    if os.path.exists(image):
        im = Image.open(image)
        new_name=im.rotate(number)
        new_name.save('Nacho.jpg')
        print(f"{image} loading.")
        new_name.show()
    else:
        print(f"{image} does not exist.")

path='/home/pablo-alimasi/Desktop/Docker/IMAGES'
for filename in os.listdir(path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        print(filename)
print('1. Rename the image.')
print('2. Resize the image.')
print('3. Rotate the image.\n')
choose=int(input('Enter your option: '))

if choose ==1: 
    image_name=input('Enter the image: ')
    new_image=input('Enter the new image name with its extension: ')
    rename_image(image_name,new_image)

elif choose ==2:
    image_name=input('Enter the image: ')
    width=int(input('Enter the width: '))
    height=int(input('Enter the height: '))
    change_resize(image_name,width,height)

elif choose == 3:
    image_name=input('Enter the image: ')
    number=int(input('Enter the Number of pixels: '))
    rotate_image(image_name,number)

