#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#Diego Benavides
#feb 27 2022
#Midterm


import numpy as np
import matplotlib.pyplot as plt

def planet_tour( start , destination ):
    """This function will take in the given starting location and the given destination location, and return the
    distance between the two locations for the best case and the time taken to travel between them 
    moving at 0.001 AU/hr for the best case.
    The function also returns how many stops of refueling are required, and makes a .txt file to send to 
    the stations mentioning where the refueling stops are needed. It also prints the date for the best case with the 
    distance for the best case of each refuel stop with a 4 digit precision.
    
    INPUT: start location input at the beginning of the code, destination location input in the beginning 
    OUTPUT: distance between the two inputs for the best case, 
            and the travel time between the two places with a speed of 0.001 AU/hr for the best case"""
    
    planets_and_moons = ['Mercury' , 'Venus' , 'Earth' , 'Moon' , 'Ceres' , 'Mars' , 'Jupiter' , 'Io' , 'Europa' , 'Saturn' , 'Titan' , 'Neptune' , 'Pluto' , 'Charon']
    
    start_location = start
    
    destination_location = destination
    
    
    if start_location in planets_and_moons:
        if destination_location in planets_and_moons:
            print(f'Both {start_location} and {destination_location} are valid locations. The Journey will proceed!\n')
        else:
            print(f'One or more of your locations is invalid.\nYour possible options are {planets_and_moons}.\nInput new locations:\n')
            new_start_location = str(input())
            new_destination_location = str(input())
    else:
        print(f'One or more of your locations is invalid.\nYour possible options are {planets_and_moons}.\nInput new locations:\n')
        new_start_location = str(input())
        new_destination_location = str(input())
        
        
    
    space_distances_date_1 = np.loadtxt('solar_system_date_1.dat', comments = '#')
    space_distances_date_2 = np.loadtxt('solar_system_date_2.dat', comments = '#')
    space_distances_date_3 = np.loadtxt('solar_system_date_3.dat', comments = '#')

    start_body_i = planets_and_moons.index(start_location)
    destination_body_i = planets_and_moons.index(destination_location)

    distance_date_1 = space_distances_date_1[ destination_body_i , start_body_i ]

    distance_date_2 = space_distances_date_2[ destination_body_i , start_body_i ]

    distance_date_3 = space_distances_date_3[ destination_body_i , start_body_i ]
    
    
    list_of_distances = [ distance_date_1 , distance_date_2 , distance_date_3]


    best_date_distance = np.min(list_of_distances)
    

    if distance_date_1 == best_date_distance :
        best_date = 'Date 1'
        
    if distance_date_2 == best_date_distance :
        best_date = 'Date 2' 
        
    if distance_date_3 == best_date_distance :
        best_date = 'Date 3'
    
    best_case_total_distance = f"The best date to travel is {best_date} , the distance is %.4f AU." % (best_date_distance)
    
    print(f'The best date to travel is {best_date} , the distance is %.4f AU.' % (best_date_distance))
    
    refuel_distance = 0.65
    
    expected_stops = np.ceil((( best_date_distance / refuel_distance)-1))
    
    
    total_distance = f"Your total travel distance is {best_date_distance} AU"
    
    average_speed = 0.001
    travel_time_years = (best_date_distance/average_speed) / (24*365)
    travel_time_days =  (travel_time_years - int(travel_time_years)) * 365
    travel_time_hours = (travel_time_days - int(travel_time_days)) * 24
    travel_time_minutes = (travel_time_hours - int(travel_time_hours)) * 60
    
    travel_time = f"Your trip will take {int(travel_time_years)} year(s), {int(travel_time_days)} day(s), {int(travel_time_hours)} hour(s), and {int(travel_time_minutes)} minute(s)"
    
    print(f'\n{travel_time}')
    
    print(f"\nYour journey will require {expected_stops} refueling stops.")
    
    f = open( "message_to_stations.txt" , 'w' )
    
    if expected_stops >= 1:
        
        arr_of_stops = np.arange( 1 , expected_stops+1)
        
        f.write(f"My trip starts at {start_location} and ends at {destination_location}. ")
        
        for i in range(len(arr_of_stops)):
            f.write(f"I will need to encounter a stop at %.4f AU.\n" % (arr_of_stops[i] * 0.65))
            
        print('\n')
        
    if expected_stops < 1:
        
        f.write("No stops needed for your trip.\n")
        
    f = open("message_to_stations.txt" , 'r')
    
    output_message = f.read()
    
    print(output_message)
    
    f.close()
    
    return ( best_case_total_distance , travel_time )



