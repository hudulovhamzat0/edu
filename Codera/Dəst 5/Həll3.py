a=input()
def hudul(f):
    if len(f)<10:
        print("Təhlükəli parol")
        exit()
    if len(list(set(a)))<4:
        print("Təhlükəli parol")
        exit()        
    print("Təhlükəsiz parol")
hudul(a)