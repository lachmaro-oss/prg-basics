Ean = input('enter code EAN 13 digits: ')

#print(Ean[0])
#print(len(Ean))
#if Ean == 13: 
 #   print('Your code have 13 digits')

if len(Ean) == 13 :
    print('Article number is correct') 
else:
    print('Article number isnt correct')

if Ean[0] == "5" and Ean[1] == "9" and Ean[2] == "0":
    print("Article manufactured in Poland")
else:
    print('Article not manufactured in Poland')
