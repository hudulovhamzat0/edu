def hudul(n):
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i
            return (i, j)
    return None

n=int(input())
print(hudul(n))