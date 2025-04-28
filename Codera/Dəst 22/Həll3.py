def hudul(a, b):
    def ati242(a, b):
        while b:
            a, b = b, a % b
        return a

    ebob_degeri = ati242(a, b)
    ekob_degeri = a * b // ebob_degeri
    return ebob_degeri + ekob_degeri

a,b=list(map(int,input().split()))
print(hudul(a,b))