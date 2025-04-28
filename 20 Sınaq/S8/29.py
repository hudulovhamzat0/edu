def hudul(s):
    num = ''
    total = 0
    for c in s:
        if c.isdigit():
            num += c
        else:
            if num:
                total += int(num)
                num = ''
    if num:
        total += int(num)
    return total

text = input()
print(hudul(text))