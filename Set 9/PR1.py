def search(data_list,element):
    for item in data_list:
        if item == element:
            return True
    else:
        return False

data_list=[int(x) for x in input("Enter list: ").split()]
element = int(input("Enter element to find: "))
if search(data_list,element):
    print("\nElement Found.")
else:
    print("\nElement not found.")
    