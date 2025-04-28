a=input()
hudul=''
for char in a:
    hudul=hudul+char+'1'
hudul=hudul[:len(hudul)-1:1]
hudul=int(hudul)
print(hudul)
print(pow(hudul,2))