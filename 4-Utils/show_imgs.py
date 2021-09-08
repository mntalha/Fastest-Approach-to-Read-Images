# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 20:54:09 2021

@author: talha
"""
import numpy as np
import matplotlib.pyplot as plt

def show_imgs(dataset):
    fig = plt.figure(figsize=(28, 28))
    for i in range(1,21):
        idx = np.random.randint(100)
        fig.add_subplot(4,5,i)
        plt.imshow(dataset.data[idx])
    plt.show()
