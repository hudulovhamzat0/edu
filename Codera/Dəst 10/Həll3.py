i=0
hudul=[]
while i < 101:
    s=0
    for reqem in str(i):
        s=s+int(reqem)
    if s==10:
        hudul.append(i)
    i=i+1
print(hudul)