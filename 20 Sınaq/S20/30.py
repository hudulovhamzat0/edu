def sade(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

a = list(map(int, input().split()))
for i in a:
    eks = int(str(i)[::-1])
    cem = i + eks
    if sade(cem):
        print(i)
