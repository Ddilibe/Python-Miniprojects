#!/usr/bin/env python
"""
	Script that explores the video capabilities of opencv
"""

import numpy as np
import cv2 as cv

cap = cv.VideoCapture("videoplayback.mp4")
if not cap.isOpened():
	print("Cannot open camera")
	exit()
while True:
	# Capture frame-by-frame
	ret, frame = cap.read()

	# if frame is read correctly ret is True
	if not ret:
		print("Can't receive frame (stream end?), Exiting...")
		break
	# Our operations on the frame comes here
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	# Display the resulting frame
	cv.imshow('frame', gray)
	if cv.waitKey(0) == ord('q'):
		break

# When everything is done, release the capture
cap.release()
cv.destroyAllWindows()