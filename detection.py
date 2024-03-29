# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 11:27:23 2021

@author: gta4s
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def line_detection(image, edge_image, num_rhos=180, num_thetas=180, t_count=91):
    edge_height, edge_width = edge_image.shape[:2]
    edge_height_half, edge_width_half = edge_height / 2, edge_width / 2
    #
    d = np.sqrt(np.square(edge_height) + np.square(edge_width))
    dtheta = 180 / num_thetas
    drho = (2 * d) / num_rhos
    #
    thetas = np.arange(0, 180, step=dtheta)
    rhos = np.arange(-d, d, step=drho)
    
    # rhos = x * sin(thetas) + y* cos(thetas)
    
    sin_thetas = np.sin(np.deg2rad(thetas))
    cos_thetas = np.cos(np.deg2rad(thetas))
    
    # An array accumulator which will count the occurance in hough space for a 
    # (rho,theta) pair for all edge points on the edge image
    accumulator = np.zeros((len(rhos),len(rhos)))
    
    for y in range(edge_height):
        for x in range(edge_width):
            if edge_image[y][x] != 0:
                  edge_point = [y - edge_height_half, x - edge_width_half]
                  ys, xs = [], []
                  for theta_idx in range(len(thetas)):
                      rho = (edge_point[1] * cos_thetas[theta_idx]) + (edge_point[0] * sin_thetas[theta_idx])
                      theta = thetas[theta_idx]
                      rho_idx = np.argmin(np.abs(rhos - rho))
                      accumulator[rho_idx][theta_idx] += 1
   
    # Iterate through the accumulator and find the rho,theta pair which is above some
    # threshold value. draw line using those rho and theta values on top of the give image.
    
    figure = plt.figure(figsize = (3,3))
    subplot1 = figure.add_subplot(1,2,1)
    subplot1.imshow(image)
    #subplot2 = figure.add_subplot(1,2,2)
    #subplot2.imshow(edge_image)
    for y in range(accumulator.shape[0]):
        for x in range(accumulator.shape[1]):
            if accumulator[y][x] > t_count:
                rho = rhos[y]
                theta = thetas[x]
                a = np.cos(np.deg2rad(theta))
                b = np.sin(np.deg2rad(theta))
                x0 = (a*rho) + edge_width_half
                y0 = (b*rho) + edge_height_half
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))
                subplot1.add_line(mlines.Line2D([x1, x2],[y1, y2]))
                
                
    plt.show()            
    return accumulator, rhos, thetas      

image = cv2.imread("image1.png")
edge_image = cv2.Canny(image, 50, 75)
line_detection(image, edge_image)      
                
    