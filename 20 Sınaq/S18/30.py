a = list(map(int, input().split()))
h = []
for i in a:
    s = 0
    for char in str(i): 
        s += int(char)
    if s > 12:
        h.append(i)
print(h)
