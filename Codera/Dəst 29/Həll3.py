def hudul(x):
    x=str(x)
    sum1=int(x[0])+int(x[1])
    sum2=int(x[2])+int(x[3])
    if sum1==sum2:
        return True
    else:
        return False
i=1000
while i<10000:
    if hudul(i):
        print(i)
    i=i+1