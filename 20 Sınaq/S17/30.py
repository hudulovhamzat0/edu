a=input().split()
h=[]
q=''
for el in a:
    h.append(len(el))
for i in h:
    q=q+str(i)
q=int(q)
print(q)