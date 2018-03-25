def sumOf(numbers):
    sum = 0
    for num in numbers:
        sum+=num
    return sum

numbers = list(float(x) for x in input('Enter numbers to find sum: ').split())
print(sumOf(numbers))