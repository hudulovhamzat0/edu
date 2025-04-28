a=input()

hudul=True

for char in a:
    if int(char)%2==0:
        hudul=False

if hudul:
    print('Hamısı təkdir')
else:
    print('Hamısı tək deyil')