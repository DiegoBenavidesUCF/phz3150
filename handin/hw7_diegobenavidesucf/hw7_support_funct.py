#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# Diego Benavides

# Feb 20 2022

# Homework 7

import numpy as np
import matplotlib.pyplot as plt


def circle( x , x0 , y0 , r ):
    """ This fucntion takes in a numpy array x, the coordinates of the center of the circle (x0,y0), and a radius r. the function returns
    all y coordinates of the circle with radius r.
    INPUT: x coordinate array, x0 coordinate, y0 coordinate, radius r
    OUTPUT: y coordinate array"""
            
    y = np.sqrt(np.abs((np.power(r,2))-(np.power((x - x0),2))))+ y0
    
    return y

def order_array( input_array ):
    """This function will take an array of numbers and sort them by numerical order
    without using an built in functions on python such as .max() .min() or .sort().
    INPUT: Not ordered array of numbers
    OUTPUT: array of numbers that is in numerical order"""
    
    for i in range(len( input_array )):
        
        for j in range(i + 1, len( input_array )):
            
            if (input_array[i] > input_array[j]):
                
                input_array[i] , input_array[j] = input_array[j] , input_array[i]
                
        
    return input_array



