#positional parameter example
def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('{}: {}'.format(message,values_str))

log('numers',[1,2,5,6.8])
log('No numbers')

#Default argument example
def sumOf(numbers=[0]):
    total_sum = 0
    for x in numbers:
        total_sum += x
    return total_sum

print(sumOf([1,2,3,4,5]))
print(sumOf())