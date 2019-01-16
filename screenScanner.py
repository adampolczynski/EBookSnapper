import cv2
import numpy as np
import threading

import utils

def scanIt(interval):
	threading.Timer(int(interval), scanIt, [interval]).start()

	utils.takeScreenshot()
	img = utils.getImage(len(utils.images) - 1)

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# define range of white color in HSV
	lower_white = np.array([0, 0, 0], dtype=np.uint8)
	upper_white = np.array([0,0,255], dtype=np.uint8)

	# Threshold the HSV image to get only white colors
	mask = cv2.inRange(hsv, lower_white, upper_white)
    # Bitwise-AND mask and original image
	output = cv2.bitwise_and(img,img, mask= mask)

	# get contours
	imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(imgray,127,255,0)
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	# find the biggest area
	c = max(contours, key = cv2.contourArea)
	x,y,w,h = cv2.boundingRect(c)
	print('Biggest contours, w:%d, h:%d' % (w, h))

	# calculate ratio
	ratio = round(h/w, 2)
	print('Ratio h/w: %f' % ratio)

	# draw the book contour (in green)
	cv2.rectangle(output,(x,y),(x+w,y+h),(0,255,0),2)

	roi = img [y:y+h, x:x+w]
	# cv2.imwrite("ROI.jpg", roi)

	print('Interval screenshot taking #%d, isBookPage:%r' % (len(utils.images), ratio == 1.41))

    # if (ratio == 1.41):
    #     return True