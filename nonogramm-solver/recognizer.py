#!/usr/bin/env python

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path='digital.jpg'
plot_flag=True
save_output=True
out_folder='outs'
os.makedirs(out_folder,exist_ok=True)

image=cv2.imread(image_path)

def plot(image,cmap=None):
    plt.figure(figsize=(15,15))
    plt.imshow(image,cmap=cmap)

if plot_flag:
    plot(image)
