a = list(map(int, input().split()))
total = sum(a)
for i in range(len(a)):
    a[i] = total - a[i]
print(a)
