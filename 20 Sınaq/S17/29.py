a=input()

s=0

for char in a:
    s=s+int(char)

if s>5:
    print('+')
else:
    print('-')