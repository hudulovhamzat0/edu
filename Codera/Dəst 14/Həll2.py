kabab,plov,baliq=map(int, input().split())
if kabab>plov and kabab>baliq:
    print('kabab')
elif plov>kabab and plov>baliq:
    print('plov')
else:
    print('baliq')
