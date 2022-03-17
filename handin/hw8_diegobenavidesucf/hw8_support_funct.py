#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Diego Benavides
#Mar 15 EST 2022
#Hw8

import numpy as np

def kepler_3rd( period ):
    """This function takes in orbital period in days and converts it into years and returns the distance from the sun in AU
    INPUT: The orbital period in days given by the table in problem 2.
    OUTPUT: The distance from sun in AU."""
    
    p_years = period / 365.25
    
    p_years_squared = np.power( p_years , 2 )
    
    a = np.power( p_years_squared , 1/3 )
    
    return a


def piston( V , P0 , V0 , T0 , gamma ):
    """This function takes in an array of volumes, inital pressure, initial volume, and initial temperature, and gamma 
    in order to calculate the array of pressures and array of temperatures. The function returns the arrays of 
    pressure, volume and temperature in a 3D array. I transposed the array so that the columns are the pressure, volume and temperature
    not the rows."""
    #for the array of pressures:
    
    constant_1 = P0*V0/T0
    
    P_new = constant_1 / np.power(V,gamma)
    
    #for the temperatures:
    
    constant_2 = P0*(np.power(V,gamma))
    
    T_new = P_new*V/constant_2
    
    return np.transpose(np.array([P_new , V , T_new]))

