def hudul(lst):
    m = c = 1
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            c += 1
            m = max(m, c)
        else:
            c = 1
    return m

lst = list(map(int, input().split()))
print(hudul(lst))
