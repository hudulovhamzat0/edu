def hudul(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

a=list(map(int,input().split()))

b=[]

for element in a:
    elem=str(element)
    if hudul(int(elem[0])+int(elem[len(elem)-1])):
        b.append(element)
print(b)