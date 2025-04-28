a=input()
hudul=[]
i=0
for char in a:
    if char=="0" or char=="1" or char=="2" or char=="3" or char=="4" or char=="5" or char=="6" or char=="7" or char=="8" or char=="9":
        hudul.append(i)
    i=i+1

for element in hudul:
    print(element)