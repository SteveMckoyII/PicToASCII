import os.path
import numpy as np
import imageio

from PIL import Image,ImageDraw,ImageFont
from math import trunc

def convert_image(input_file, output_file):
	#assigns size
	image_width = 1000
	image_height = 500
	#opens and converts image to grayscale
	img = Image.open(input_file).convert("L")
	#resizes image
	img = img.resize((image_width, image_height))

	#converts image to array of pixels
	pixel_array = np.array(img)
	#assigns characters to pixel values
	ASCII = ['.',',','*','^','!','|','+','-',';','o','x','%','?','$','#','@']

	f = open(output_file, 'w')

	for x in pixel_array:
		for y in x - 1:
			f.write(ASCII[trunc(y/255*17)-1])
		f.write('\n')
	f.close()
	return True

convert_image('picture.png', 'picutre.text')