###
# Sums numbers entered by user
#
total_sum = 0
arithmaticmean = 0 
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
        
    total_sum += number
    arithmaticmean = total_sum / number

print(f"The total sum of the numbers is: {total_sum} and arithamitc mean of this numer is {arithmaticmean}")