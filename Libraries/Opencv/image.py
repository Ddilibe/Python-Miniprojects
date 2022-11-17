#!/usr/bin/env python
"""
	Script thar explores the reading, displaying and writing an image file using Opencv windows
"""

import cv2 as cv
import sys
import os

if os.path.exists('images'):
	url = 'images/1.jpeg'
	file = cv.samples.findFile(url)
	img = cv.imread(file)

	if img is None:
		sys.exit("Could not read the image")

	cv.imshow("Dislay windows", img)
	k = cv.waitKey(0)

	print(k, ord("s"))
	
	if k == ord("s"):
		cv.imwrite("images/1.png", img)