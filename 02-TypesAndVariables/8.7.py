###
# A program that converts a decimal number
# into binary and hexadecimal format.
#
number = int(input('Enter number: '))

binary_number = bin(number)
hexadecimal_number = hex(number)

print(f'Binary number: {binary_number}')
print(f'Hexadecimal number: {hexadecimal_number}')