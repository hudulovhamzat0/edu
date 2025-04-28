a = input().split()
a = list(reversed(a))

h=''

for word in a:
    h=h+word+' '

print(h)