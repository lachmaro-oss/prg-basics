#washing_product = "shoes"
#rinse = True
#spin = False
#Total washing time: 35 minutes

washing_product = input("select product that you want to wash (shoes , jacket , underwear): ")
rinse = input("Do you want additional rinse? (+15min) Y/N: ")
spin = input("Do you want additional spins? (+9min) Y/N: ")

if rinse == 'Y':
    rinse = True
elif rinse == "N":
    rinse = False

if  spin == 'Y':
    spin = True
elif spin == "N": 
    spin = False
#print(bool(rinse),bool(spin))

if washing_product == "shoes" and bool(rinse) == False and bool(spin) == False:
    print('Total washing time 20 minutes')
elif washing_product == "shoes" and bool(rinse) == True and bool(spin) == False:
    print('total washing time 35 minutes ')
elif washing_product == "shoes" and bool(rinse) == True and bool(spin) == True:
    print("total washin time 44 minutes")

if washing_product == "jacket" and bool(rinse) == False and bool(spin) == False:
    print('Total washing time 40 minutes')
elif washing_product == "jacket" and bool(rinse) == True and bool(spin) == False:
    print('total washing time 55 minutes ')
elif washing_product == "jacket" and bool(rinse) == True and bool(spin) == True:
    print("total washin time 64 minutes")


if washing_product == "underwear" and bool(rinse) == False and bool(spin) == False:
    print('Total washing time 70 minutes')
elif washing_product == "underwear" and bool(rinse) == True and bool(spin) == False:
    print('total washing time 85 minutes ')
elif washing_product == "underwear" and bool(rinse) == True and bool(spin) == True:
    print("total washin time 94 minutes")