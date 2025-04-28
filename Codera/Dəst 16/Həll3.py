a=list(map(int, input().split()))
for i in a:
    if i > a[a.index(i)-1] and i > a[a.index(i)+1]:
        print(a.index(i))