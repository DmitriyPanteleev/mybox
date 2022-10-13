import cv2
import numpy as np
import easyocr

im_1_path = './test2.png'

def recognize_text(img_path):
    '''loads an image and recognizes text.'''
    
    reader = easyocr.Reader(['en'])
    return reader.readtext(img_path)

result = recognize_text(im_1_path)
print(result)
