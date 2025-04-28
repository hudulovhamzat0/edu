a=input()
h=[]
hudul=""
for i in a:
    h.append(int(i))
h=sorted(h)
for i in h:
    hudul=hudul+str(i)
print(hudul)