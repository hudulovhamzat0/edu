def hudul(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

T=map(list(int,input().split()))

if hudul(max(T)+min(T)):
    print('Yes')
else:
    print('No')