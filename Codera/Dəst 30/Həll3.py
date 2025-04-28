a=str(input())

hudul=[]

for i in a:
    hudul.append(int(i))
hudul.remove(max(hudul))

res=''
for char in hudul:
    res=res+str(char)

print(res)