def hudul(a, b):
    def ebob(a, b):
        while b:
            a, b = b, a % b
        return a

    ortaq_bolenler = []
    ebob_degeri = ebob(a, b)
    
    for i in range(1, ebob_degeri + 1):
        if a % i == 0 and b % i == 0:
            ortaq_bolenler.append(i)
    
    return ortaq_bolenler

a,b=list(map(int,input().split()))
print(hudul(a,b))