# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 22:02:54 2021

@author: talha
"""

import matplotlib.pyplot as plt
 
# x-coordinates of left sides of bars
left = [1, 2, 3, 4]
 
# heights of bars
height = [2.27, 0.95, 2.01, 3.79]
 
# labels for bars
tick_label = ['MATPLOTLIB', 'CV2', 'PIL', 'SKIMAGE']
 
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['yellow', 'green','blue','red'])
 
# naming the x-axis
plt.ylabel('Elapsed Time')
# naming the y-axis
plt.xlabel('Modules')
# plot title
plt.title('Speed Comparison')
 
# function to show the plot
plt.show()