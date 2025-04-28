a=input()

def hudul(x):
    if len(x)%2==0:
        return False
    return True
if hudul(a): print(a[len(a)//2]), exit()
print("Orta rəqəm yoxdur")