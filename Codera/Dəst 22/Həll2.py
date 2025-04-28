def hudul(n):
    if n <= 0:
        return False
    while n % 8 == 0:
        n //= 8
    return n == 1

n=int(input())

if hudul(n):
    print(n)
else:
    print('-')