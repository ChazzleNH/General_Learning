#!/usr/bin/env python3

import os
import glob
from PIL import Image

size = 128, 128

files = glob.glob('ic_*')

# Opens each image file line by line and rotates them 90 clockwise, resizes to 128x128
# then converts them to jpeg and saves them in the path opt/icons/

for file in files:
    wrong_picture = Image.open(file).convert('RGB')
    wrong_picture.rotate(-90).resize((size)).save('/opt/icons/' + file, 'JPEG')    

print('complete')






