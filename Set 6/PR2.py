try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c = a/b
except ValueError as e:
    print('Input is not a nuumber: '+str(e))
except ZeroDivisionError as e:
    print('Error: b (divider) cannot be zero.')
else:
    print('Division is: {}'.format(c))