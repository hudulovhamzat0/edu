n=list(map(int,input().split()))

for i in range(len(n)):
    for j in range(i+1, len(n)):
        print(f"Element: {n[i]}, Sonrakı elementin indexi: {j}")
