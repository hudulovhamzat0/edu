a,b,c=list(map(int, input().split()))
qaliq_pul=a-b

if c/qaliq_pul==c//qaliq_pul:
    gun=c//qaliq_pul
else:
    gun=c//qaliq_pul+1
print(gun)