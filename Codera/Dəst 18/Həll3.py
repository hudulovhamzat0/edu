n=list(map(int,input().split()))
hudul=[]

for i in n:
    hudul.append(int(str(i)[0])+int(str(i)[len(str(i))-1]))
print(hudul)