import icao
name = input('Enter your name: ')
print('ICAO words for spelling out your name:')

for char in name:
    word = icao(char)
    print(word, end=" ") 
