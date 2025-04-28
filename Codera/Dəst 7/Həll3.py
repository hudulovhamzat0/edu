def hudul(y):
    dumb_list=[]
    for i in y:
        dumb_list.append(int(i))
    if len(dumb_list)==dumb_list.count(dumb_list[0]): return True
a=input()
if hudul(a): print("Hamısı eynidir"), exit()
print("Bütün rəqəmlər eyni deyil")