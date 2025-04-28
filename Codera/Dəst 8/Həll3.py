a,l,b=input().split()

def hudul(q,w,e):
    q=int(q)
    e=int(e)
    if w=='+':
        return q+e
    elif w=='-':
        return q-e
    elif w=='*':
        return q*e
    elif w=='/':
        return q/e

res=hudul(a,l,b)
print(res)