def swap(num):
    n1, n2 = num
    return n2, n1
numbers= list(int(x) for x in input('Enter 2 numbers to swap them: ').split())
num = numbers[0], numbers[1]
print(swap(num))