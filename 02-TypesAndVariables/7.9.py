#Dice rolled: 4
#Special number (1 or 6): False
import random



dice_roll_1 = random.randint(1,8)

dice_roll_2 = random.randint(1,8)


dice_roll_3 = random.randint(1,8)


dice_roll_4 = random.randint(1,8)

special = dice_roll_1 == 1 or 6 and dice_roll_2 == 1 or 6 and dice_roll_3 == 1 or 6 and dice_roll_4 == 1 or 6 
sum  = dice_roll_1 + dice_roll_3 + dice_roll_2 + dice_roll_4
print(sum) 
print(f'special number: {special}')
