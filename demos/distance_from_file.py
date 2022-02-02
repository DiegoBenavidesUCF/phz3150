def distance_from_file2( t , u ):
    """This is function calculates the distance traveled by object mobing with speed u [ m / s ] 
    during time t [ s ].
    Input ( t , u ) / Output s [ m ]  """
    
    s = u * t
    
    print( 'Moves', s , 'm')
    return s
 


def my_tshirt_forecast( temperature, cloudiness ):
    """ Predicts if you can wear a t-shirt based on temperature and cloudiness. 
    Input: temperature [ F ] , cloudiness [ % ] 
    Output: Yes / No """
    
    if temperature < 70 :
        print( " No! " )
        
    if temperature > 70 : 
        if cloudiness > 50 :
            print (" No! ")
        else : 
            print ( " Yes! ")
    
    