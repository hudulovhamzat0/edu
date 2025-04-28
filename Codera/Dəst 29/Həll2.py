a=input()
ati=len(a)
h=''
i=0

while i<ati-1:
    h=h+a[i+1]
    i=i+1
h=h+a[0]
print(h)