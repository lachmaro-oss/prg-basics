#1Read a decimal number from the keyboard.
#2Divide the number by 2 and note the remainder.
#3Divide the quotient obtained by 2 and note the remainder.
#4Repeat the same process till we get 0 as the quotient.
#5Write the values of all the remainders starting from the bottom to the top. That will be the required binary number.
#Sample result:
#Enter decimal number: 12
#12(10) = 1100(2)

decimal_number = float(input("enter decimal number: "))
division = decimal_number / 2
print(f'first reminder {division}')  
division1 = division / 2 
print(f'second divison {division1}')