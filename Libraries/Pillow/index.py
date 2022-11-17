#!/usr/bin/env python3
"""
Script for testing out python3 pillow environment.
"""

from PIL import Image
import PIL

"""
	Open() function is used to read an image file
	show() function is used to display the image respectively.
	"""
img = Image.open("<name_of_audio_file>")
img.show()

"""
	size - attribute provides the size of the image. It returns a tuple that contains width and height.
	format - attribute returns the format of the image file
"""

print(img.size) # Returns a tuple with height and width of the image
print(img.format) # Returns the format of the image
print(img.mode) # Function that returns the color mode of the image

"""
	rotate() method of the Image class is used to rotate the image by a particular angle counterclockwise around its center.
	After rotating the image, the sections of the image having no pixel values are filled with black (for non-alpha images) 
	and with completely transparent pixels (for images supporting transparency).
"""
img2 = img.rotate(90, PIL.Image.NEAREST, expand=1)
