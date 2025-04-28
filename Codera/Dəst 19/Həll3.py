def hudul(number):
    digits = list(str(number))
    max_digit = max(digits)
    min_digit = min(digits)
    
    result = ''.join([max_digit if d == min_digit else min_digit if d == max_digit else d for d in digits])
    
    return result

number = int(input())
print(hudul(number))
