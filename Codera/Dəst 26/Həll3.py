def faktorial_tapan(n):
    r=1
    for i in range(2,n+1):r*=i
    return r

#Proqramın 2 versiyası var 
# 1) sətir kimi düstur verən
# 2) hesablayan

n=int(input())
i=0
s=''
while i<2*n:
    i=i+2
    s=s+str(i)+'!/'+'x**'+str(i)+'+'
s=s[:-1]
print(s)