a = list(map(int, input().split()))
hudul = []

for i, element in enumerate(a):
    if i % 2 != 0 and element % 2 == 0:
        hudul.append(int(oct(element)[2:]))

print(hudul)
