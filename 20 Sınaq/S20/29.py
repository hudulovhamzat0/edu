a=input().split()
hudul=[]
for i in a:
    b=len(i)-1
    i=i.replace(str(i[b]),str(len(i)-1))
    hudul.append(i)
print(hudul)