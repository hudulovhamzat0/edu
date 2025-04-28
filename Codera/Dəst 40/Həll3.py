def hudul(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

ededler = list(map(int, input().split()))
say = 0
for eded in ededler:
    cem = sum(map(int, str(eded)))
    if hudul(cem):
        say += 1
print(say)
