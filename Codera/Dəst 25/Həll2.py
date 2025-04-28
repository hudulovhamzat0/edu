h = list(map(int, input().split()))

h.remove(min(h))
h.remove(max(h))

print(max(h) + min(h))
