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
reader = easyocr.Reader(['en'])
result = reader.readtext(args["image"])

# result
pprint(result)
