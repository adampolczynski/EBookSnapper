import cv2
import numpy as np
import pyautogui
import imutils

images = []

def takeScreenshot():
	image = pyautogui.screenshot()
	image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
	images.append(image)
	return image
	
def showImage(index):
	if len(images) < index:
		print('No such image\n')
		return
	#cv2.imwrite("scr.png", images[index])
	cv2.imshow("Screenshot", imutils.resize(images[index], width=600))
	cv2.waitKey(0)
	
def getImage(index):
	if len(images) < index:
		print('No such image\n')
		return
	return images[index]