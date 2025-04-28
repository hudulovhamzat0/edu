a=input()
hudul=''
for char in a:
    if char=='0' or char=='1' or char=='2' or char=='3' or char=='4' or char=='5' or char=='6' or char=='7' or char=='8' or char=='9':
        hudul=hudul+char*int(char)
    elif char.upper()==char:
        pass
    elif char.lower()==char:
        hudul=hudul+char.upper()
print(hudul)