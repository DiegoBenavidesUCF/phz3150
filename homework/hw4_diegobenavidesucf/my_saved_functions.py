#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#Diego Benavides
#Homework 4 Problem 3
#Feb 2 2022

def acceleration( u1 , u2 , t1 , t2 ):
    """This function will calculate acceleration from dividing its change in velocity[m/s] by the change in time[s]
    or in other words its getting acceleration by calculating the rate of change of velocity
    INPUT: Initial velocity, final velocity, inital time, final time.
    OUTPUT: Acceleration[m/s^2]"""
    
    a = (u2 - u1)/(t2 - t1)
    
    return a



