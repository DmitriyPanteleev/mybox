# import the necessary packages
import argparse
import cv2
import numpy as np
import easyocr
from pprint import pprint

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
args = vars(ap.parse_args())

# ocr-ing
image = cv2.imread(args["image"])
#crop_image = image[50:2000, 20:1060]
#grayImage = cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)
#(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
#cv2.imwrite('/home/user/SomeStuff/mybox/nonogramm-solver/crop_bw_img.png', blackAndWhiteImage)
reader = easyocr.Reader(['en'])
result = reader.readtext(image[50:2000, 20:1060], allowlist='0123456789', detail=0)

# result
pprint(result)
