
###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#

light_switch1 = False # True = włączony, False = wyłączony
light_switch2 = True  # True = włączony, False = wyłączony

bulbs_on = 0

if light_switch1:
    bulbs_on += 1

if light_switch2:
    bulbs_on += 2

print(f'Total bulbs on: {bulbs_on}')