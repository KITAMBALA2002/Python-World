#!/usr/bin/env python3

import os
from PIL import Image

print('A PROJECT FOR MODULE 1 OF THE FINAL CAPSTONE\n')

input_folder = '/home/pablo-alimasi/Pictures/Module1'
output_folder = '/home/pablo-alimasi/Desktop/Practical'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)

    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        with Image.open(file_path) as img:
            rotated_img = img.rotate(-90, expand=True)
            resized_img = rotated_img.resize((128, 128))

            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')
            resized_img.save(output_path, 'PNG')
            
print("Image processing completed.")

#checking the file size extension
with Image.open('style.png')as img:
    print(img.format,img.size)
