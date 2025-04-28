def hudul(x):
    n = 1
    f = 1
    while f < x:
        n += 1
        f *= n
    return f == x

a=int(input())

if hudul(a):
    print('Bəli')
else:
    print('Xeyr')