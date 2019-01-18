import cv2
import numpy as np
import threading
import pyautogui
from fpdf import FPDF

import utils

def scanIt(interval):
	threading.Timer(int(interval), scanIt, [interval]).start()

	img = utils.takeScreenshot()

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

	ratioFits = ratio > 1.35 and ratio < 1.45
	print('Interval screenshot taking #%d, isBookPage:%r' % (len(utils.images), ratioFits))

	if ratioFits:
		utils.images.append(roi)
		imgPath = './pics/ROI%d.jpg' % len(utils.images)
		cv2.imwrite(imgPath, roi)		
		pyautogui.press('right')
		if (roi == utils.images[len(utils.images) - 1]).all:
			print('Saving images as pdf...')
			pdf = FPDF()
			# imagelist is the list with all image filenames
			for index, val in enumerate(utils.images):
				pdf.add_page()
				pdf.image('./pics/ROI%d.jpg' % int(index + 1))
			pdf.output("./pdfs/output.pdf", "F")
			print('Success saving pdf!')