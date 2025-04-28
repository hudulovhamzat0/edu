def hudul(n):
    ati, b = 0, 1
    while b <= n:
        ati, b = b, ati + b
    return b

ati242=int(input())
print(hudul(ati242))