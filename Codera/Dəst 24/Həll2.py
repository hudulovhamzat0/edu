a=int(input())

def f(n):
    r=1
    for i in range(2,n+1):r*=i
    return r

def check_fact(u):
    i=1
    s=0
    hudul=0
    while s < u:
        s=s*i+1
        i=i+1
        hudul=hudul+1
    if f(hudul)==u:
        print(hudul)
    else:
        print("-")

check_fact(a)