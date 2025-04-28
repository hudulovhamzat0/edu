n=list(map(int,input().split()))

def hudul(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

italy=[]

for element in n:
    if not hudul(element):
        italy.append(element)

s=0
for element in italy:
    s=s+int(element)
s=s/len(italy)
print(s)