def hudul(x):
    if x<=1:
        return False
    if x==2:
        return False
    if x%2==0:
        return False
    for i in range(3,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
n=int(input())
if hudul(n):
    print("Sadə ədəddir")
else:
    print('Mürəkkəb ədəddir')