list_1=input("Enter 1st list:\n").split()
list_2=input("\nEnter nd list:\n").split()
list_1.extend(list_2)
print("\nConcated list:\n {}".format(list_1))
