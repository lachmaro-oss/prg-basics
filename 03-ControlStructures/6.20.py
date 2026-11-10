decimal_number = int(input("Enter decimal number: "))
original_number = decimal_number

binary_str = ""

if decimal_number == 0:
    binary_str = "0"
else:
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_str = str(remainder) + binary_str
        decimal_number = decimal_number // 2

print(f"{original_number}(10) = {binary_str}(2)")