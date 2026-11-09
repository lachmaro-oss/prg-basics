question1 = input('SURVEY Are you interested in computer science? (y/n)')
question2 = input('Do you like playing computer games? (y/n)')
question3 = input('Do you have an Instagram account? (y/n):')

if question1 == "y":
    question1 = True
elif question1 == "n":
    question1 = False
#print(bool(question1))

if question2 == "y":
    question2 = True
elif question2 == "n":
    question2 = False
#print(bool(question2))

if question3 == "y":
    question3 = True
elif question3 == "n":
    question3 = False
#print(bool(question3))

if bool(question1) == True:
    print('SURVEY RESULTS Interested in computer science: Yes')
elif bool(question1) == False:
    print(('SURVEY RESULTS Interested in computer science: No'))

if bool(question2) == True:
    print('Playing computer games: Yes')
elif bool(question2) == False:
    print(('Playing computer games: No'))

if bool(question2) == True:
    print('Has an Instagram account: Yes')
elif bool(question2) == False:
    print(('Has an Instagram account: No'))