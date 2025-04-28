a=input().split()
h=[]
for i in a:
    h.append(i[0])
    h.append(i[len(i)-1])
    h.append(' ')

hudul=''

for i in h:
    hudul=hudul+i

print(hudul)