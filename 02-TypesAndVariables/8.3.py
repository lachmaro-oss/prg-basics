###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# ...
# ...
# ...

enterTEMPinCelcius = float(input('enter temp in celsius:'))
#using input function to write down vaule of celcius from keybord  also float to converts the specified value into a floating point number
farenheit = enterTEMPinCelcius*1.8
farenheit2 = farenheit + 32 
Kelvin = enterTEMPinCelcius + 273.15
#using math operations to change celsius for a farenheit and kelvin
print(f'celsius temp {enterTEMPinCelcius} farenheit temp {farenheit2} kelvin temp {Kelvin}')
#printing with f string to show direct value of changed temperatures 