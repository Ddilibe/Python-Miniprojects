#!/usr/bin/env python
"""
	Script that attempts creating a video from a series of pictures
"""

import numpy as np
import cv2 as cv
import random
import sys
import os

if not os.path.exists('video'):
	os.mkdir('video')

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('video/new.avi', fourcc, 1, (640, 480), isColor=True)

while True:
	url = ['images/0.jpeg', 'images/1.jpeg', 'images/2.jpeg']
	file = cv.samples.findFile(url[random.randint(0, 2)])
	img = cv.imread(file)

	frame = cv.flip(img, 0)

	out.write(frame)

	cv.imshow("Video", frame)
	if cv.waitKey(1) == ord("q"):
		break

out.release()
cv.destroyAllWindows()
