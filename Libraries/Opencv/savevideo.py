#!/usr/bin/env python
"""
	Script that explores the video saving objects
"""

import numpy as np
import cv2 as cv

cap = cv.VideoCapture("videoplayback.mp4")

if not cap.isOpened():
	print("Can't open Camera")
	exit()

# Define the codec and create VieoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480), isColor=True)

while cap.isOpened():
	ret, frame = cap.read()
	if not ret:
		print("Can't receive frame (stream end?). Exiting...")
		break
	frame = cv.flip(frame, 0)

	# Write the flipped frame
	out.write(frame)

	cv.imshow("Frame", frame)
	if cv.waitKey(1) == ord('q'):
		break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()