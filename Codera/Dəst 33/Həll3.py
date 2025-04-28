def hudul(o):
    i=1
    hasil=1
    while hasil<o:
        i=i+1
        hasil=hasil*i
    if hasil==o:
        return i
    else:
        return -1

h=int(input())
h=hudul(h)+1
print(h)