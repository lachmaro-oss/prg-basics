#Write a program that calculates a dog's age in dog's years. For the first two years, a dog's life is equal to 10.5 human years. After that, each dog year is equal to 4 human years. Sample result:

#Enter the dog's age in human years: 15
#The dog's age in dog's years is 73 years.

dogageinhuman = int(input('Enter the dogs age in human years:'))
dogyears = 0 
 
aftertwoyears = dogyears  


if dogageinhuman == 2:
    dogyears = 21
elif dogageinhuman == 1:
    dogyears = 10.5
elif  dogageinhuman > 2:
    dogageinhuman = dogageinhuman - 2
    dogyears = 21 + 4*(dogageinhuman) 

print(dogyears)