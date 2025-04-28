ededler = list(map(int, input().split()))
cem = 0
for eded in ededler:
    cem += sum(map(int, str(eded)))
print(cem)
