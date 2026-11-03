
first = input('Enter first letter: ')
last = input('Enter last letter: ')

first_letter_code = ord(first)
last_letter_code = ord(last)

difference = abs(last_letter_code - first_letter_code)
number_of_letters = max(0, difference - 1)

print(f'Between {first} and {last} is {number_of_letters} letters')