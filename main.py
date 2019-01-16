# import the necessary packages
#from skimage.measure import compare_ssim
import argparse
import imutils
import cv2

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
#menuPrompt()

def scanIt():
	threading.Timer(5.0, scanIt).start()
	ss.takeScreenshot()
	img = ss.getImage(len(ss.images) - 1)
	print('Interval screenshot taking #' + str(len(ss.images)))

scanIt()