import change

# Reads employee's data from keyboard
first_name = change.input_string('Enter name: ')
last_name = change.input_string('Enter Last Name: ')
age = change.input_integer('Enter your age: ')
salary = change.input_real('Enter your salary: ')
is_salary_hidden = change.input_boolean('Hide salary? (y/n): ')

# Prints employee's record
print('DATA RECORD')
print('===========')
print(f'Name: {first_name}')
print(f'Last Name: {last_name}')
print(f'Age: {age}')
if not is_salary_hidden:
    print(f'Salary: {salary}')