para=input()
s1=0
s2=0
for char in para:
    if char=="0" or char=="1" or char=="2" or char=="3" or char=="4" or char=="5" or char=="6" or char=="7" or char=="8" or char=="9":
        s1=s1+1
    else:
        s2=s2+1
print(s1*s2)