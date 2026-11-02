import math

height_of_the_observer_in_meters = float(input('Input height of the observer in meters: '))
distance_to_the_horizon_in_kilometers = 3.57 * math.sqrt(height_of_the_observer_in_meters)
print(f'Distance to the horizon: {distance_to_the_horizon_in_kilometers:.2f} km')


my_height = 1.95
distance_my_height = 3.57 * math.sqrt(my_height)
print(f'Distance for height {my_height} m: {distance_my_height:.2f} km')


hotel_height = 20
distance_hotel = 3.57 * math.sqrt(hotel_height)
print(f'Distance for hotel window (20 m): {distance_hotel:.2f} km')