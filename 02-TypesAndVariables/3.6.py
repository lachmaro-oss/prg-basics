import math 

distance_to_the_horizon_in_kilometers = float(input('input distance to the horizon in kilometers:'))
height_of_the_observer_in_meters = float(input('input height of the observer in meters:'))

distance_to_the_horizon_in_kilometers = 3.57 * math.sqrt(height_of_the_observer_in_meters)

print(f'{distance_to_the_horizon_in_kilometers }km')


myheight = 1.95 
disatnce_betwenmeandhorizon = 3.57 * math.sqrt(myheight)
print(f'{disatnce_betwenmeandhorizon} km.')