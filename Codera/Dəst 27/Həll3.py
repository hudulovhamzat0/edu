def hudul(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b

n = int(input())
hudul(n)
