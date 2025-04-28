n=int(input())
found=False
for i in range(int(pow(n,0.5))+1):
    for h in range(i,int(pow(n,0.5))+1):
        if pow(i,2)+pow(h,2)==n:
            found=True
            print(i,h)
            exit()

if not found:
    print('-')