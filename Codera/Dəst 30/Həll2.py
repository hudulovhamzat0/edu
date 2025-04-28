def hudul(n):
    x = n + 1
    while True:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                break
        else:
            return x
        x += 1

n = int(input())
print(hudul(n))
