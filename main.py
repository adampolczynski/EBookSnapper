# import the necessary packages
# from skimage.measure import compare_ssim
import argparse
import imutils
import cv2
import numpy as np
import threading

# our files
import screenshot as ss

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
# ap.add_argument("-f", "--first", required=True,
# 	help="first input image")
# ap.add_argument("-s", "--second", required=True,
# 	help="second")
args = vars(ap.parse_args())

userInput = 0


def menuPrompt():
	print('\nMenu\n')
	print('1. Take screenshot and store in memory\n')
	print('2. Show photo from memory by index\n')
	print('3. Get photo by index and crop\n')

	userInput = int(input('Chose it [1-3]!\n'))

	if userInput == 1:
		image = ss.takeScreenshot()
		menuPrompt()

	if userInput == 2:
		index = int(input('Provide index\n'))
		ss.showImage(index)
		menuPrompt()
	if userInput == 3:
		index = int(input('Provide index\n'))
		image = ss.getImage(index)
		w, h = image.size
		image.crop((0, 30, w, h-30))
# menuPrompt()
def find_border_components(contours, ary):
    borders = []
    area = ary.shape[0] * ary.shape[1]
    for i, c in enumerate(contours):
        x,y,w,h = cv2.boundingRect(c)
        if w * h > 0.5 * area:
            borders.append((i, x, y, x + w - 1, y + h - 1))
    return borders



def scanIt():
	#threading.Timer(5.0, scanIt).start()

	ss.takeScreenshot()
	img = ss.getImage(len(ss.images) - 1)

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# define range of white color in HSV
	lower_white = np.array([0, 0, 0], dtype=np.uint8)
	upper_white = np.array([0,0,255], dtype=np.uint8)

	# Threshold the HSV image to get only white colors
	mask = cv2.inRange(hsv, lower_white, upper_white)
    # Bitwise-AND mask and original image
	res = cv2.bitwise_and(img,img, mask= mask)

	edges = cv2.Canny(np.asarray(img), 100, 200)

	imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(imgray,127,255,0)
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	borders = find_border_components(contours, edges)

	newImg = cv2.drawContours(img, contours, -1, (0,255,0), 3)

	cv2.namedWindow("Screenshot", cv2.WINDOW_AUTOSIZE)
	cv2.imshow("Screenshot", newImg)
	cv2.waitKey(0)
	# ss.showImage(len(ss.images) - 1)
	print('Interval screenshot taking #' + str(len(ss.images)))

scanIt()


