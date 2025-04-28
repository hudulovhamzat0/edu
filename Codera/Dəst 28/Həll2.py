ati=input()
s=0

for num in ati:
    s=s+int(num)
s=s/len(ati)

hudul=''
for num in ati:
    if int(num)>s:
        hudul=hudul+str(num)
print(hudul)