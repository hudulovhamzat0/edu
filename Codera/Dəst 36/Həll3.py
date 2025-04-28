a=input().split()
i=1

def hudul(word):
    for i in word:
        print(i)

for word in a:
    if i==len(a):
        break
    if len(word)<len(a[i]):
        hudul(word)
    i=i+1