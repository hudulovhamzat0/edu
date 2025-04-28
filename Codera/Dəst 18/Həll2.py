def hudul(n):
    return sum(int(digit) for digit in str(n))
def hudulov(numbers):
    divisible_elements = []
    for i in range(len(numbers) - 1):
        current_number = numbers[i]
        next_number = numbers[i + 1]
        if next_number % hudul(next_number) == 0:
            divisible_elements.append(current_number)
    return divisible_elements

numbers = list(map(int,input().split()))
result = hudulov(numbers)
print(result)
