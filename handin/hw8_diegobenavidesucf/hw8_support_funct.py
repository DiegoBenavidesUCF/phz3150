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



