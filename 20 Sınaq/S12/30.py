def hudul(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

a,b=map(int,input().split())

if hudul(a) and hudul(b):
    print('Yes')
else:
    print('No')