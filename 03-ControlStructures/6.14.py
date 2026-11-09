#influencer = input('whats your social media?: choose from: (facebook , twitter , instagram): ')
facebook = input('are you using facebook? Y/N ')
if facebook == "Y":
    facebook = True
elif facebook == "N":
    facebook = False
#print(bool(facebook))
                
instagram = input('are you using instagram? Y/N ')
if instagram == "Y":
    instagram = True
elif instagram == "N":
    instagram = False
#print(bool(instagram))

twitter = input('are you using twitter? Y/N ')
if twitter == "Y":
    twitter = True
elif twitter == "N":
     twitter = False
#print(bool(twitter))

if facebook == True and instagram == True and twitter == False:
    print(f'Your good influancer!!!')
    print(f'facebook = {facebook}')
    print(f'insagram = {instagram}')
    print(f'twitter = {twitter}')
elif facebook == False and instagram == False and twitter == True:
    print('Your bad influancer')
    print(f'facebook = {facebook}')
    print(f'insagram = {instagram}')
    print(f'twitter = {twitter}')
elif facebook == True and instagram == False and twitter == False:
    print('Your bad influancer')
    print(f'facebook = {facebook}')
    print(f'insagram = {instagram}')
    print(f'twitter = {twitter}')
elif facebook == False and instagram == True and twitter == False:
    print('Your bad influancer')
    print(f'facebook = {facebook}')
    print(f'insagram = {instagram}')
    print(f'twitter = {twitter}')
elif facebook == True and instagram == False and twitter == True:
    print('Your good influancer')
    print(f'facebook = {facebook}')
    print(f'insagram = {instagram}')
    print(f'twitter = {twitter}')
elif facebook == False and instagram == False and twitter == False:
    print('Your bad influancer')
    print(f'facebook = {facebook}')
    print(f'insagram = {instagram}')
    print(f'twitter = {twitter}')


