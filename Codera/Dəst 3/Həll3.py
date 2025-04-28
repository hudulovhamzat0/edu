a=list(map(int, input().split()))

def hudul(x):
    x=str(x)
    dumb=int(x[0])+int(x[1])
    dumb2=int(x[1])+int(x[2])
    if dumb>dumb2:
        return (str(dumb)+str(dumb2))
    else:
        return (str(dumb)+str(dumb2))

for i in a:
    if hudul(i)=="1217":
        print("Alınır", i)
    else:
        print("Alınmır")