a=input()
hudul=[]
s=0
for reqem in a:
    hudul.append(int(reqem))
hudul.remove(max(hudul))
for reqem in hudul:
    s=s+reqem
print(s)