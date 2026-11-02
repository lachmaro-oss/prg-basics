#The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. Write a program that checks whether the vehicle speed entered from the keyboard is correct. Sample result:

#Enter vehicle speed: 158
#Speed is valid: False

speedV = int(input("Enter vehicle speed:"))

iscorretcS = speedV >= 40 and speedV <= 140 

print(f"Speed i valid:{iscorretcS}")