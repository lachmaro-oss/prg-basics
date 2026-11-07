#The parking meter calculates the parking fee based on the number of hours the car was parked according to the following rules:

#1-2 hours: 5 PLN
#3-6 hours: 15 PLN
#Over 6 hours: 20 PLN
#Write a program that asks for the number of hours of parking, then calculates and prints the correct fee.

howmanthours = int(input('how many hours are you gonna park?:'))
if howmanthours == 1 or howmanthours == 2:
    print('fee is 5 PLN')
elif howmanthours == 3 or howmanthours == 4 or howmanthours == 5 or howmanthours == 6:
    print('fee is 15PLN')
elif howmanthours > 6:
    print('parking fee is 20PLN')