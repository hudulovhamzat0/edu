alphabet = "abcdefghijklmnopqrstuvwxyz"

text = input("Mətni daxil edin: ")
n = int(input("N ədədini daxil edin: "))

encrypted_text = ""

for char in text:
    index = alphabet.index(char)
    new_index = (index + n) % len(alphabet)
    encrypted_text += alphabet[new_index]

print("Şifrələnmiş mətn:", encrypted_text)
