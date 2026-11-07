#Most female names in Polish end with the letter "a". Write a program that prints the name entered from the keyboard, provided it is a female name. Sample result:

#Enter name: Anna
#Anna -- Polish female name

name = input('whats your name?')

if name[-1] == 'a':
    print(f'{name} --  Polish female name')
else:
    print('not a polish woman')