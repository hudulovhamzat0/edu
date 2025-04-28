a=list(map(int,input().split()))
a.remove(max(a))
a.remove(min(a))
print(max(a)+min(a))