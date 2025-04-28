a=input()
g=[]
for i in a:
    if int(i)%2==0:
        g.append(int(i))
print(max(g))