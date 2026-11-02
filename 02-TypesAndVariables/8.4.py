###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170
feet = cm / 30.48
inches1 = cm % 2.54
inches = cm / 2.54
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches1} inches')