a=input()
for char in a:
    if int(char)%2==0:
        x=(int(char)*3)%10
    else:
        x=(int(char)*2)%10
    a=a.replace(str(char),str(x))
print(a)