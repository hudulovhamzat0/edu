a = list(map(int, input().split()))
p = [i for i in a if str(i) == str(i)[::-1]]
print(max(p))
