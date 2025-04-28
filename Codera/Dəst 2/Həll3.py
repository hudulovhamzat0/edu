a=input().split()
b=[]
c=0
for i in a:
    b.append(abs(int(i)))
for i in b:
    c=c+i
hudul=c/int(len(b))
if hudul>22:
    for i in a:
        print(i)
else:
    print("Böyük deyil")