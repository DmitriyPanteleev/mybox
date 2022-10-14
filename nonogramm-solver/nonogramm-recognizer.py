import cv2
import numpy as np
import easyocr
from pprint import pprint

im_1_path = '/home/dpanteleev/SomeStuff/mybox/nonogramm-solver/test2.png'

def recognize_text(img_path):
    '''loads an image and recognizes text.'''
    
    reader = easyocr.Reader(['en'])
    return reader.readtext(img_path)

result = recognize_text(im_1_path)
pprint(result)
