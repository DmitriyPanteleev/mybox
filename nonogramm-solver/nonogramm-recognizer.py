# import the necessary packages
import argparse
import cv2
import numpy as np
import easyocr
from pprint import pprint
import matplotlib.pyplot as plt

def plot(image,cmap=None):
    plt.figure(figsize=(15,15))
    plt.savefig(image) 

def imshow_components(labels):
    ### creating a hsv image, with a unique hue value for each label
    label_hue = np.uint8(179*labels/np.max(labels))
    ### making saturation and volume to be 255
    empty_channel = 255*np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, empty_channel, empty_channel])
    ### converting the hsv image to BGR image
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
    labeled_img[label_hue==0] = 0
    ### returning the color image for visualising Connected Componenets
    return labeled_img

def detect_box(image,line_min_width=15):
    gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    th1,img_bin = cv2.threshold(gray_scale,150,225,cv2.THRESH_BINARY)
    kernal6h = np.ones((1,line_min_width), np.uint8)
    kernal6v = np.ones((line_min_width,1), np.uint8)
    img_bin_h = cv2.morphologyEx(~img_bin, cv2.MORPH_OPEN, kernal6h)
    img_bin_v = cv2.morphologyEx(~img_bin, cv2.MORPH_OPEN, kernal6v)
    img_bin_final=img_bin_h|img_bin_v
    final_kernel = np.ones((3,3), np.uint8)
    img_bin_final=cv2.dilate(img_bin_final,final_kernel,iterations=1)
    ret, labels, stats,centroids = cv2.connectedComponentsWithStats(~img_bin_final, connectivity=8, ltype=cv2.CV_32S)
    return stats,labels

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
args = vars(ap.parse_args())
plot_flag=True
save_output=False

# ocr-ing
image = cv2.imread(args["image"])
#crop_image = image[50:2000, 20:1060]
#grayImage = cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)
#(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
#cv2.imwrite('/home/user/SomeStuff/mybox/nonogramm-solver/crop_bw_img.png', blackAndWhiteImage)
reader = easyocr.Reader(['en'])
result = reader.readtext(image[50:2000, 20:1060], allowlist='0123456789', detail=0)

stats,labels=detect_box(image)
cc_out=imshow_components(labels)

for x,y,w,h,area in stats[2:]:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)

if plot_flag:
    plot("./m_cc_out.png")
    plot("./mimage.png") 

# result
pprint(result)
