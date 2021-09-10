# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 21:48:53 2021

@author: talha
"""

import os


#define img_path
img_path = "../3-Data/train_img"


#check path control
if isinstance(img_path, str): #Image path is a string
    if os.path.exists(img_path):
        print ("Path is exist")
    else:
        raise FileNotFoundError('Path is not found on your system')    


#measure elapsed time
import timeit


#list the image_name
imgs_name = os.listdir(img_path) #Read the image name inside the path
img_array = []


#MATPLOTLIB READ
import matplotlib.image as mpimg
starttime = timeit.default_timer()
for img in os.listdir(img_path):
    img_array.append(mpimg.imread(os.path.join(img_path, img)))
print("The time difference is :", timeit.default_timer() - starttime)
#The time difference is : 2.2727211

# CV2 IMREAD
import cv2
starttime = timeit.default_timer()
for img in imgs_name:
    img_array.append(cv2.imread(os.path.join(img_path, img)))
print("The time difference is :", timeit.default_timer() - starttime)
#The time difference is : 0.9522216000000001


# PIL  READ
from PIL import Image
import numpy as np
starttime = timeit.default_timer()
for img in imgs_name:
    img_array.append(np.asarray(Image.open(os.path.join(img_path, img))))
print("The time difference is :", timeit.default_timer() - starttime)
#The time difference is : 2.0121553

# IO IMREAD  FROM SKIMAGE
import skimage.io as io
starttime = timeit.default_timer()
for img in os.listdir(img_path):
    img_array.append(io.imread(os.path.join(img_path, img)))
print("The time difference is :", timeit.default_timer() - starttime)
# The time difference is : 3.799766


#TorchVision
import torchvision.io as t_io
starttime = timeit.default_timer()
for img in os.listdir(img_path):
    img_array.append(t_io.read_image(os.path.join(img_path, img)))
print("The time difference is :", timeit.default_timer() - starttime)
# The time difference is : 0.943434400000001

