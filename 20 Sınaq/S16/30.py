def hudul(x):
    n = 1
    f = 1
    while f < x:
        n += 1
        f *= n
    if f == x:
        return n

a=int(input())

if hudul(a):
    print(hudul(a))
else:
    print('-')