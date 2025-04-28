a=input()
num=[]
for char in a:
    num.append(char)

test=num

test=sorted(test)
test.reverse()

if num==test:
    print('+')
else:
    print('-')
