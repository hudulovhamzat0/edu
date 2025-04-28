a=input()
num=0
spec=''
for char in a:
    if int(a.count(char))>num:
        num=int(a.count(char))
        spec=char
print(spec)