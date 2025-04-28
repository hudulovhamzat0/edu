a=input()
hudul=''
for character in a:
    if int(character)%2==0:
        hudul=hudul+character+'3'
    else:
        hudul=hudul+character+'4'
print(hudul)