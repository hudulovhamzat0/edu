a=[34,142,40,-63,85,47]
cem=0
hasil=1
for i in a:
    i=int(i)
    if i%2==0:
        cem=cem+i
    else:
        hasil=hasil*i
print(cem)
print(hasil)