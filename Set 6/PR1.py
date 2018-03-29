def calculate_pay(hours,rate):
    if hours>40:
        pay=(40*rate)+((hours-40)*(rate*1.5))
    else: pay=hours*rate
    return pay

try:
    hours=int(input("Enter hours:"))
    rate=int(input("Enter rate:"))
    print("Gross pay:\t{}".format(calculate_pay(hours,rate)))
except ValueError as e:
    print('Input is not a nuumber: '+str(e))