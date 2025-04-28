a = input("Birinci ədədi daxil edin: ")
b = input("İkinci ədədi daxil edin: ")

new_number = ""

for i in range(len(a)):
    remainder = int(a[i]) % int(b[i])
    new_number += str(remainder)

print("Yeni ədəd:", new_number)
