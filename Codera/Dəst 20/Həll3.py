i=0
while i < 101:
    a=int(input())
    if a<10 and a>7:
        print(pow(a,2)+10)
    elif a<8:
        print(pow(a,4))
    else:
        print(a*7)