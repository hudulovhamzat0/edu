# a və b siyahıları
a=list(map(int,input().split()))
b=list(map(int,input().split()))

def hudul(a, b):
    def ati242(a, b):
        while b:
            a, b = b, a % b
        return a

    ebob_degeri = ati242(a, b)
    return ebob_degeri

if len(a)!=len(b):
    print('error')
    exit()

lenght=len(a)

i=0

h=[]

while i<lenght:
    h.append(hudul(a[i],b[i]))
    i=i+1
print(h)