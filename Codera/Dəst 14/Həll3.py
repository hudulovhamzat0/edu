i=100
hudul=[]
while i<1000:
    if int(str(i)[0])%2==0 and int(str(i)[1])%2==0 and int(str(i)[2])%2==0:
        hudul.append(i)
    i=int(i)
    i=i+1
print(hudul)