n=list(map(int,input().split()))
aylar = [
    "Yanvar", "Fevral", "Mart", "Aprel", "May", "İyun",
    "İyul", "Avqust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"
]
s=0
for i in n:
    s=s+i
s=int(s/len(n))

for i in n:
    if i>s:
        print(aylar[n.index(i)])
        