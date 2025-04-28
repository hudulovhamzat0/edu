p=int(input())

def hudul(zed):
    bolenler = []
    for i in range(1, zed + 1):
        if zed % i == 0:
            bolenler.append(i)
    return bolenler

r=hudul(p)

sum=0

for i in r:
    sum=sum+i
print(sum)