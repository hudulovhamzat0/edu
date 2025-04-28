def sade_vuruqlar(n):
    vuruqlar = []
    bolen = 2
    while n > 1:
        if n % bolen == 0:
            vuruqlar.append(bolen)
            n //= bolen
        else:
            bolen += 1
    return vuruqlar

a=int(input())
print(sade_vuruqlar(a))