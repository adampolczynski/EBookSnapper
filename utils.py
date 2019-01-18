import cv2
import numpy as np
import pyautogui
import imutils

# our files
import sound

images = []

def takeScreenshot():
	image = pyautogui.screenshot()
	sound.playShutterSound()
	image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
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