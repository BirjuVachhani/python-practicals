# This problem arises from a commercial case where in a food outlet named mcdonalds
# there were three food packets containing chicken nuggets with numbers 6,9,20
# out of these packets if a customer demands for a certain number the vendor had to think 
# a lot to check whether that number was possible to deliver or not as those packets where 
# to be sold whole. Due to this the problem is named mcchicken nuggets as this problem states 
# to solve and state whether a certain number is possible using using 6,9,20 or not.

def is_buyable(quantity):
    try:
        if quantity == 0:
            return True
        elif quantity < 0 or quantity<6:
            return False
        # Through recursion it can be solved easily
        elif is_buyable(quantity - 20) or is_buyable(quantity - 9) or is_buyable(quantity - 6):
            return True
        else:
            return False
    except:
        print('An exception occured, sorry for the incovinience!')


def order_quantity():
    quantity = int(input('Hello custome, enter the number of chicken nuggets you want to purchase \n'))
    isPossible = is_buyable(quantity)
    if isPossible:
        print('Yes, you can buy this amount of chicken nuggets, enjoy your order! :) ')
    else :
        print("Sorry,you can't buy these numbers of chicken nuggets, kindly change the quantity and try again!")
    return

try:
    while True:
        order_quantity()
except KeyboardInterrupt:
    pass