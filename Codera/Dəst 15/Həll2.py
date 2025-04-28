dumb_list=[-23,18,9,-11,12,-14]
s=0
for eded in dumb_list:
    if eded%2==0 and eded>-1:
        s=s+dumb_list.index(eded)
print(s)