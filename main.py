# from skimage.measure import compare_ssim
import argparse
import pathlib

# our files
import utils
import screenScanner as ss

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--interval", required=True,
	help="Interval in seconds")
# ap.add_argument("-s", "--second", required=True,
# 	help="second")
args = vars(ap.parse_args())

userInput = 0

utils.images = []

def menuPrompt():
	print('\nMenu\n')
	print('1. Start scanner (interval: %d)\n' % int(args.get('interval')))
	print('2. Show photo from memory by index\n')
	print('3. Save %d images as pdf\n' % len(utils.images))

	userInput = int(input('Chose it [1-3]!\n'))

	if userInput == 1:
		pathlib.Path("./pics").mkdir(parents=True, exist_ok=True)
		pathlib.Path("./pdfs").mkdir(parents=True, exist_ok=True)
		ss.scanIt(args.get('interval'))
		menuPrompt()

	if userInput == 2:
		index = int(input('Provide index\n'))
		utils.showImage(index)
		menuPrompt()

	if userInput == 3:
		print('asdas')
		# pdf = FPDF()
		# # imagelist is the list with all image filenames
		# for image in utils.images:
		# 	pdf.add_page()
		# 	pdf.image(image,x,y,w,h)
		# pdf.output("yourfile.pdf", "F")

menuPrompt()


