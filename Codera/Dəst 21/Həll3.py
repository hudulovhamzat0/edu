a=list(map(int,input().split()))
def hudul(x):
    if pow(x,0.5)==int(pow(x,0.5)):
        return True
    else:
        return False

hudulov=[]

for num in a:
    if hudul(num):
        hudulov.append(num)

cem=0
for num in hudulov:
    cem=cem+int(num)
orta=cem/len(hudulov)
print(orta)