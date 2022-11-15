#!/usr/bin/env python
"""
	Script that creates multiple images from one prototypes
"""

from PIL import Image, ImageDraw
import os

if not(os.path.exists('images')):
	os.mkdir('images')

if not(os.path.exists('new')):
	os.mkdir('new')
url = "prototype/lips"
for root, dirs, file in os.walk(url):
	img, e = Image.open('prototype/background.jpg'), 0
	for i in file:
		new_image = img.copy()
		img2 = Image.open(f"{url}/{i}")
		new_image.paste(img2, (0, 0))
		new_image.save(f"new/{e}.jpeg")
		new_image.close()
		e += 1
	img.close()

