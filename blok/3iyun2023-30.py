a=[351,648,776,918]
h=[]
sum=0
for i in a:
    i=str(i)
    sum=int(i[0])+int(i[len(i)-1])
    h.append(sum)
print(h)