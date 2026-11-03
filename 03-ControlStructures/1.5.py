###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20
tasks_ok = int(input("how many tasks you done?"))
test_passed = False

if tasks_ok >= total_tasks *0.5: 
#if tasks_ok == total_tasks and tasks_ok == 19 and tasks_ok == 18 and tasks_ok == 17 and tasks_ok == 16 and tasks_ok == 15 and tasks_ok == 14 and tasks_ok == 13 and tasks_ok == 12 and tasks_ok == 11 and tasks_ok == 10:
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')
