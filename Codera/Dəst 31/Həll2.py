a = input()

hudul = [int(i) for i in a]

ez = hudul.copy()

count = 0
while count < len(ez):
    if ez[count] % 2 != 0:
        ez[count] = 0
    count += 1

big = max(ez)

yeni_a = ""
for i in hudul:
    if i % 2 != 0:
        yeni_a += str(big)
    else:
        yeni_a += str(i)

print(yeni_a)
