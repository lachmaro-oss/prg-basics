
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
sum_even = 0
x = 0 
# Calculate the sum of even numbers
#for i in range(1, N + 1):
while N >= 1 : 
    if x % 2 == 0:
        sum_even += x

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")