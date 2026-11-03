###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus = 0.15 # 15%
y = 5000 * bonus
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'

if is_bonus == "Y":
    total_salary = basic_salary + y
else:
    total_salary = total_salary 

print(f'Basic salary: {basic_salary}')
print(f'Basic salary + bonus if included: {basic_salary + y }')
print(f'Bonus included? {is_bonus}')