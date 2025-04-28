def hudul0v(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def hudul(siyahi):
    for i in range(len(siyahi)-1, -1, -1):
        if hudul0v(siyahi[i]):
            return i
    return -1

siyahi = list(map(int, input().split()))
print(hudul(siyahi))
