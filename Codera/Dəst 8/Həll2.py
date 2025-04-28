a=input()
j=[]
for i in a:
    j.append(i)
j=sorted(list(set(j)))
print(j)