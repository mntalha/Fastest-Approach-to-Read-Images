# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 20:14:12 2021

@author: talha
"""

import torch
import torchvision.datasets as datasets
import cv2 

import sys
sys.path.append('../4-Utils/')
from show_imgs import show_imgs


print(torch.__version__)

#load train data
mnist_trainset = datasets.MNIST(root='.', train=True, download=True, transform=None)


show_imgs(mnist_trainset)

import os 
#create train_img directory

directory ="../3-Data/train_img" 

if not os.path.exists(directory):
    os.makedirs(directory)

#go that directory
os.chdir(directory) 


# turn jpg format it may take several minutes because we try to save 10,000 (28x28) images
for i in range(10000):
    cv2.imwrite(str(i)+".jpg", mnist_trainset.data[i].numpy()) 

    