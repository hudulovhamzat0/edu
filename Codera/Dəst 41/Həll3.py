a=input().split()
i=0
x=999
remember=0
for word in a:
    if len(word)<x:
        x=len(word)
        remember=i
    i=i+1
my_special_cutie_word=a[remember]
my_special_cutie_word=my_special_cutie_word[::-1]
print(my_special_cutie_word)