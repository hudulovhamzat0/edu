a=input()
son=a[len(a)-1]
for i in a:
    if i==son:
        a=a.replace(i,"")
hudul=[]
for i in a:
    hudul.append(int(i))
hudul=sorted(hudul)

res=''
for i in hudul:
    res=res+str(i)

print(res)