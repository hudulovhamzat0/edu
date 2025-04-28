def hudul(num):
    return (int(num, 16))
a=input()
a=str(hudul(a))
s=0
for char in a:
    if int(char)%2==0:
        s=s+int(char)
print(s)